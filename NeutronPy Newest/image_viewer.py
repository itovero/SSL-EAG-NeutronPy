#NOTE: self.image_cube is a non-numpy array implementation at the moment!
#TODO: add a z-range selection for plotting certain subsections of the image cube

import sys, traceback
from os import listdir, path
from os.path import isfile, join
from astropy.io import fits
import numpy as np
import time
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from progress_bar import Progress

from beamline import Beamline
from TransmissionCalc import Get_E_FromTOF

class selector(QRubberBand):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 4))
        color = QColor(Qt.green)
        painter.drawRect(event.rect())


##ImageCubeLoadSignal and ImageCubeLoader is a class that assists in dumping all the data into the image cube without having to terminate the MainWindow
##Done via multi-threading
class ImageCubeLoadSignal(QObject):
    #Class to monitor the progress of loading the fits files into the image cube
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int, int, float)

class ImageCubeLoader(QRunnable):
    #Separate Thread to handle mutliprocesses 
    #This one, in particular, deals with opening each fits file and inserting them into the image cube
    def __init__(self, fn, *args, **kwargs):
        super(ImageCubeLoader, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

        self.signals = ImageCubeLoadSignal()
        self.kwargs['progress_callback'] = self.signals.progress

    
    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except: 
            #Handles exception if there's an issue with loading data
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


##Image_viewer is the actual image GUI we see on the top left of the screen
class image_viewer(QGraphicsView):
    rect_sig = pyqtSignal(QRect)

    def __init__(self):
        super().__init__()
        self.empty = True
        self.zoom = 0
        self.max_zoom = 7
        self.scene = QGraphicsScene(self)
        self.photo = QGraphicsPixmapItem()
        self.scene.addItem(self.photo)
        self.setScene(self.scene)
        self.setBackgroundBrush(QBrush(QColor(30, 30, 30)))

        self.rect = selector(QRubberBand.Rectangle, self)

        #Stores the rectangle geometry relative to scene
        self.rect_scene = QRect()
        self.rect_change = False
        self.rect_exists = False


    def show_photo(self):
        rect = QtCore.QRectF(self.photo.pixmap().rect())
        self.setSceneRect(rect)

    def set_photo(self, pixmap=None):
        self.zoom = 0
        if self.rect_exists:
            self.update_rect()
        if pixmap and not pixmap.isNull():
            self.empty = False
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self.photo.setPixmap(pixmap)
            self.show_photo()

    def update_rect(self):
        top_left = self.mapFromScene(self.rect_scene.topLeft())
        bottom_right = self.mapFromScene(self.rect_scene.bottomRight())
        self.rect.setGeometry(QRect(top_left, bottom_right))

    def fit_to_window(self):
        self.zoom = 0
        viewrect = self.viewport().rect()
        imagerect = self.transform().mapRect(self.photo.pixmap().rect())
        factor = min(viewrect.width() / imagerect.width(), viewrect.height() / imagerect.height())
        self.scale(factor, factor)

    def wheelEvent(self, event):
        if (not self.rect_change):
            if event.angleDelta().y() > 0:
                self.zoom += 1
                if (abs(self.zoom) < self.max_zoom):
                    self.scale(1.25, 1.25)
                else:
                    self.zoom = self.max_zoom
            else:
                self.zoom -= 1
                if (abs(self.zoom) < self.max_zoom):
                    self.scale(0.75, 0.75)
                else:
                    self.zoom = -self.max_zoom

            if (self.zoom == 0):
                self.fit_to_window()

            self.update_rect()

    def mousePressEvent(self, event):
        if (self.photo.isUnderMouse()):
            self.origin = event.pos()
            self.rect.setGeometry(QRect(self.origin, QSize()))
            self.rect.show()
            self.rect_sig.emit(self.rect.geometry())
            self.rect_change = True
        QGraphicsView.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if (self.photo.isUnderMouse()):
            if self.rect_change == True:
                self.rect.setGeometry(QRect(self.origin, event.pos()).normalized())
                self.rect_sig.emit(self.rect.geometry())
        QGraphicsView.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.rect_change = False
        self.rect_exists = True
        top_left = self.mapToScene(self.rect.geometry().topLeft())
        bottom_right = self.mapToScene(self.rect.geometry().bottomRight())
        self.rect_scene = QRect(QPoint(top_left.x(), top_left.y()), QPoint(bottom_right.x(), bottom_right.y()))
        QGraphicsView.mouseReleaseEvent(self, event)

    def resizeEvent(self, event):
        self.update_rect()
        QGraphicsView.resizeEvent(self, event)

    # def showFileName(self, sampleFileName, openBeamDirectory = "None"):
    #     self.scene.addWidget(QLabel(sampleFileName + "          Open Beam:"  + openBeamDirectory))

class ImageViewerWindow(QWidget):
    def __init__(self, beamline):
        super().__init__()

        #Load main's instance of beamline
        self.beamline = beamline
        self.flightpath = self.beamline.saveInput()[0]
        self.delayontrigger = self.beamline.saveInput()[1]

        #For multi-threading data loadout
        self.threadpool = QThreadPool()

        self.viewer = image_viewer()
        self.files = None
        self.dir = "."

        #Load button: Opens directory selection for Sample Data
        self.loadsample_button = QToolButton(self)
        self.loadsample_button.setText('Select Sample Data')
        self.loadsample_button.clicked.connect(self.loadsample_dir)
        self.sampledirnamelabel = QLabel("None Selected")

        #Load button: Opens directory selection for Sample Data
        self.loadopenbeam_button = QToolButton(self)
        self.loadopenbeam_button.setText('Select OpenBeam Data')
        self.loadopenbeam_button.clicked.connect(self.loadopenbeam_dir)
        self.openbeamdirnamelabel = QLabel("None Selected")

        # #Backcoef value
        # self.backcoef_label = QLabel("Backcoef")
        # self.backcoef = QDoubleSpinBox()
        # self.backcoef.setValue(0)
        # self.backcoef.valueChanged.connect(self.update_backcoef)


        #Coordinates of the selection rectangle and their labels
        self.x_min_label = QLabel("X Min")
        self.x_min = QSpinBox()

        self.x_max_label = QLabel("X Max")
        self.x_max = QSpinBox()

        self.y_min_label = QLabel("Y Min")
        self.y_min = QSpinBox()

        self.y_max_label = QLabel("Y Max")
        self.y_max = QSpinBox()

        self.z_start_label = QLabel("Z Start")
        self.z_start = QSpinBox()

        self.z_end_label = QLabel("Z End")
        self.z_end = QSpinBox()
    

        self.z_label = QLabel("Current Z")
        self.z = QSpinBox()
        self.z.setMinimum(0)
        self.z.valueChanged.connect(self.load_new_image_z)


        #Update values based on changes in both the viewer and the spinboxes
        self.viewer.rect_sig.connect(self.update_xy)
        self.x_min.valueChanged.connect(self.update_rect)
        self.y_min.valueChanged.connect(self.update_rect)
        self.x_max.valueChanged.connect(self.update_rect)
        self.y_max.valueChanged.connect(self.update_rect)

        #Update values of z start and z end
        self.z_start.setValue(0)
        self.z_start.valueChanged.connect(self.update_zrange)
        self.z_end.valueChanged.connect(self.update_zrange)

        #Contrast Slider
        self.slider_label = QLabel("Contrast")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(255)

        #Update on Contrast Change
        self.slider.valueChanged.connect(self.load_new_image_scroll_bar)

        #Scroll bar
        self.scroll_bar = QSlider(Qt.Horizontal)
        self.scroll_bar.setOrientation(Qt.Horizontal)
        self.scroll_bar.setMinimum(0)
        self.scroll_bar.setMaximum(0)
        self.scroll_bar.valueChanged.connect(self.load_new_image_scroll_bar)

        #Add the image viewer and scroll bar
        layout = QVBoxLayout(self)
        vwidget = QWidget(self)
        VB = QVBoxLayout(self)
        VB.addWidget(self.viewer)
        VB.addWidget(self.scroll_bar)

        #Add the buttons to select file and backcoef 
        fileSelectRow = QHBoxLayout(self)

        fileLayout = QGridLayout(self)
        fileLayout.setAlignment(Qt.AlignLeft)
        fileLayout.addWidget(self.loadsample_button, 1, 0)
        fileLayout.addWidget(self.sampledirnamelabel, 1, 1)
        fileLayout.addWidget(self.loadopenbeam_button, 2, 0)
        fileLayout.addWidget(self.openbeamdirnamelabel, 2, 1)
        fileSelectRow.addLayout(fileLayout, 60) 

        # CoefLayout = QGridLayout(self)
        # CoefLayout.addWidget(self.backcoef_label, 1, 0)
        # CoefLayout.addWidget(self.backcoef, 2, 0)
        # fileSelectRow.addLayout(CoefLayout, 5) 

        CurrentzLayout = QGridLayout(self)
        CurrentzLayout.addWidget(self.z_label, 1, 0)
        CurrentzLayout.addWidget(self.z, 2, 0)
        fileSelectRow.addLayout(CurrentzLayout, 5)

        #Add the coordinates
        HB = QVBoxLayout(self)

        xlabelLayout = QHBoxLayout(self)
        xlabelLayout.addWidget(self.x_min_label, 50)
        xlabelLayout.addWidget(self.x_max_label, 50)
        xLayout = QHBoxLayout(self)
        xLayout.addWidget(self.x_min, 50)
        xLayout.addWidget(self.x_max, 50)
        ylabelLayout = QHBoxLayout(self)
        ylabelLayout.addWidget(self.y_min_label, 50)
        ylabelLayout.addWidget(self.y_max_label, 50)
        yLayout = QHBoxLayout(self)
        yLayout.addWidget(self.y_min, 50)
        yLayout.addWidget(self.y_max, 50)
        zlabelLayout = QHBoxLayout(self)
        zlabelLayout.addWidget(self.z_start_label, 50)
        zlabelLayout.addWidget(self.z_end_label, 50)
        zLayout = QHBoxLayout(self)
        zLayout.addWidget(self.z_start, 50)
        zLayout.addWidget(self.z_end, 50)
        HB.addLayout(xlabelLayout)
        HB.addLayout(xLayout)
        HB.addLayout(ylabelLayout)
        HB.addLayout(yLayout)
        HB.addLayout(zlabelLayout)
        HB.addLayout(zLayout)
        
        
        HB.addWidget(self.slider_label)
        HB.addWidget(self.slider)
        
        


        layout.addLayout(VB) #NOTE: In case if you're wondering where the "QLayout: Attempting to add QLayout "" to ImageViewerWindow "", which already has a layout" error is happening, it's these three lines of layout.addLayout. I (Yuki) haven't really found a way to remove this but it seems to override it so it should be non-problematic.
        layout.addLayout(fileSelectRow)
        layout.addLayout(HB)


    
    def loadsample_dir(self):
        self.dir = str(QFileDialog.getExistingDirectory(self, "Select Sample Data Directory"))

        if path.isdir(self.dir): 
            self.files = listdir(self.dir)

            pathArr = self.dir.split('/')
            self.sampledirnamelabel.setText(pathArr[-1])
            self.sampledirnamelabel.setStyleSheet("border: 1px solid black;")
            self.sampledirnamelabel.adjustSize()

            self.scroll_bar.setMaximum(len(self.files) - 1)
            self.z.setMaximum(len(self.files) - 1)
            self.load_new_image(0)

            #Initialize z range ranges
            self.z_start.setValue(0)
            self.z_end.setMaximum(len(self.files) - 1)
            self.z_end.setValue(len(self.files) - 1)
            self.z_start.setMinimum(0)
            self.z_start.setMaximum(self.z_end.value() - 1)
            self.z_end.setMinimum(self.z_start.value() + 1)


            #instantiate the TOF and image cube!
            self.TOF = []
            self.image_cube = []
            self.Ntrigs = []


            #loads every image file in the directory into an image cube containing information
            #on each pixel of each slice of data
            #For debugging, looking at the load_new_images method will be helpful as abstractions
            #are omitted for this list comprehension to maintain fastest runtime
            def load_image_cube(progress_callback):
            
                #Take the data from all the fits files and dump them into an array
                startTimer1 = time.perf_counter()
                fileLen = len(self.files)
                for fileNum in range(0, fileLen):
                    with fits.open(self.dir + '/' + self.files[fileNum], memmap = True) as hdul:
                        # if (fileNum == 0):
                        #     self.N_trigger = hdul[0].header["N_TRIGS"]
                        # else:
                        #     print(fileNum)
                        #     assert self.N_trigger == hdul[0].header["N_TRIGS"], "Number of triggers inconsistent within sample data"
                        self.image_cube.append(hdul[0].data)
                        self.TOF.append(hdul[0].header["TOF"])
                        self.Ntrigs.append(hdul[0].header["N_TRIGS"])
                        del hdul[0].data
                        if (fileNum - 1) * 100 // fileLen  != fileNum * 100 // fileLen:
                            progress_callback.emit(fileNum / fileLen * 100, 1, 0)
                endTimer1 = time.perf_counter()
                progress_callback.emit(100, 1, 0)
                time.sleep(.5)
                progress_callback.emit(100, 2, endTimer1 - startTimer1)
                time.sleep(1.5)


                '''
                #Initializing Image Cube into a Numpy Array
                startTimer2 = time.perf_counter()
                progress_callback.emit(100, 3, 0)
                '''
                
                #NOTE: uncomment these blocks for other needed operations other than sum
                #self.image_cube = np.array(self.image_cube) #this apparently takes a long time ~7.6 s for 2600 fits files
                
                '''
                endTimer2 = time.perf_counter()
                progress_callback.emit(100, 4, endTimer2 - startTimer2)
                time.sleep(2)
                '''
                
                #Close the loading window
                progress_callback.emit(100, 5, 0)

            #Naive Approach: This method literally takes in all the pixel arrays found on the fits file and shoves them into an image_cube
                #Pros: This method is great as the runtime of you selecting a region and computing the sum becomes way faster beacause it took everything in from the beginning
                #Cons: This method might suffer from some poor runtime to dump all the fits file into an image cube but doesn't seem too much of a problem at the moment
            def naive_load_data():
                #loading bar
                self.loadingBar = Progress()
                cubeThread = ImageCubeLoader(load_image_cube)
                cubeThread.signals.progress.connect(self.loadingBar.setValue)
                self.threadpool.start(cubeThread)
            
            naive_load_data() #In the case runtime becomes an issue, take a look at the compressed_load_data function and implementation
                              #Similar to naive_load_data(), it has its pros and cons - personally in my (Yuki's) opinion, naive_load_data() does better



            #Compressed Approach: 
                #We create a image cube 3D array with NaN values and instantiate them as we access the ones we desire
            """
            def compressed_load_data():
            """


    def loadopenbeam_dir(self): #Almost identical to sample data file select therefore many comments are omitted
        self.beam_dir = str(QFileDialog.getExistingDirectory(self, "Select OpenBeam Directory"))

        if path.isdir(self.beam_dir): 
            self.beam_files = listdir(self.beam_dir)
            self.openbeam_TOF = []
            self.openbeam_image_cube = []
            self.openbeam_Ntrigs = []

            pathArr = self.beam_dir.split('/')
            self.openbeamdirnamelabel.setText(pathArr[-1])
            self.openbeamdirnamelabel.setStyleSheet("border: 1px solid black;")
            self.openbeamdirnamelabel.adjustSize()

            def load_image_cube(progress_callback):
            
                #Take the data from all the fits files and dump them into an array
                startTimer1 = time.perf_counter()
                fileLen = len(self.beam_files)
                for fileNum in range(0, fileLen):
                    with fits.open(self.beam_dir + '/' + self.beam_files[fileNum], memmap = True) as hdul:
                        self.openbeam_TOF.append(hdul[0].header["TOF"])
                        self.openbeam_Ntrigs.append(hdul[0].header["N_TRIGS"])
                        self.openbeam_image_cube.append(hdul[0].data)
                        del hdul[0].data
                        if (fileNum - 1) * 100 // fileLen  != fileNum * 100 // fileLen:
                            progress_callback.emit(fileNum / fileLen * 100, 1, 0)
                endTimer1 = time.perf_counter()
                progress_callback.emit(100, 1, 0)
                time.sleep(.5)
                progress_callback.emit(100, 2, endTimer1 - startTimer1)
                time.sleep(1.5)
                progress_callback.emit(100, 5, 0)
            def naive_load_data():
                self.loadingBar = Progress()
                cubeThread = ImageCubeLoader(load_image_cube)
                cubeThread.signals.progress.connect(self.loadingBar.setValue)
                self.threadpool.start(cubeThread)
            naive_load_data()

    # Loads a new image from the image library
    #   This load_new_image is only for the image viewing purposes - it only loads and 
    #   shows one slice each for optimizing runtime while scrolling the z-bar
    def load_new_image(self, value):
        if self.files != None:
            filename = self.dir + '/' + self.files[value]

            hdul = fits.open(filename)

            image_data = hdul[0].data
            image_data = image_data / image_data.max()
            image_data = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data)) * (255 - self.slider.value())
            image_data = image_data.astype(np.uint8)

            hdul.close()

            h,w = image_data.shape
            qimage = QImage(image_data.data, h, w, QImage.Format_Grayscale8)

            self.viewer.set_photo(QPixmap(qimage))

            self.viewer.fit_to_window()

            bottom_right = self.viewer.mapToScene(self.viewer.viewport().rect().bottomRight())
            self.x_min.setMaximum(bottom_right.x())
            self.y_min.setMaximum(bottom_right.y())
            self.x_max.setMaximum(bottom_right.x())
            self.y_max.setMaximum(bottom_right.y())

    # Changed the value of  z to obtain next image
    def load_new_image_z(self):
        value = self.z.value()
        #self.viewer.showFileName(self.dir)
        self.scroll_bar.setValue(value)
        self.load_new_image(value)

    # Changed the value of the scroll_bar to obtain next image
    def load_new_image_scroll_bar(self):
        value = self.scroll_bar.value()
        self.z.setValue(value)
        self.load_new_image(value)


    # Update the values of the x and y coordinates based on the scene  (aka the image)
    def update_xy(self, rect):
        top_left = self.viewer.mapToScene(rect.topLeft())
        bottom_right = self.viewer.mapToScene(rect.bottomRight())
        self.x_min.setValue(top_left.x())
        self.y_min.setValue(top_left.y())
        self.x_max.setValue(bottom_right.x())
        self.y_max.setValue(bottom_right.y())

    def update_rect(self):
        rect_new = QRect(QPoint(self.x_min.value(), self.y_min.value()), QPoint(self.x_max.value(), self.y_max.value()))
        top_left = self.viewer.mapFromScene(rect_new.topLeft())
        bottom_right = self.viewer.mapFromScene(rect_new.bottomRight())
        self.viewer.rect_scene = rect_new
        self.viewer.update_rect()
        return [self.x_min.value(), self.x_max.value(), self.y_min.value(), self.y_max.value()]

    # def update_backcoef(self):
    #     return self.backcoef.value()

    def update_zrange(self):
        return [self.z_start.value(), self.z_end.value()]


    #Save Input function for main.py integration
    def saveInput(self): #returns = [[xmin, xmax], [ymin, ymax], [z_start, z_end], z, backcoef, self.sumImageCube, self.TOF]
        try:
            #backcoef
            #backcoef = self.update_backcoef()

            #z : SliceNum
            z = float(self.scroll_bar.value())

            #z range
            z_start, z_end = self.update_zrange()
            
            #xmin, xmax are the x coordinates of the rectangle user selected; same goes for y
            xmin, xmax, ymin, ymax = self.update_rect()

            #update beamline params
            self.flightpath = self.beamline.saveInput()[0]
            self.delayontrigger = self.beamline.saveInput()[1]

            #account TOF with the delay on trigger
            self.TOF = np.array(self.TOF)
            self.TOF += self.delayontrigger

            #load the E array from the TOF values
            self.E = Get_E_FromTOF(self.TOF, self.flightpath)

            def naive_sum_data(): 
                try: #When we have both open beam data set and sample data image cube
                    backcoef = np.array(self.openbeam_Ntrigs) / np.array(self.Ntrigs)
                    backcoef = np.array(backcoef)
                    self.sumImageCube = [backcoef[sliceNum] * np.sum((self.image_cube[sliceNum])[ymin:ymax, xmin:xmax]) / np.sum((self.openbeam_image_cube[sliceNum])[ymin:ymax, xmin:xmax]) for sliceNum in range(z_start, z_end + 1)]
                    #TODO: This runs into runtime warning of dividing by zero - fix that! Also add operations with normalization coef
                    assert self.TOF == self.openbeam_TOF, "The TOFs between the openbeam and the sample data is inconsistent! "
                    
                except: #When we don't have an open beam data set
                    #sumImageCube is the sum of all the pixel values of the rectangle you selected for all the slices in the image_cube you created when selecting the directory
                    self.sumImageCube = [np.sum((self.image_cube[sliceNum])[ymin:ymax, xmin:xmax]) for sliceNum in range(z_start, z_end + 1)]
                    
                    
                    #NOTE: uncomment these blocks for other needed operations other than sum
                    #self.sumImageCube = np.array([np.sum((self.image_cube[sliceNum])[ymin:ymax, xmin:xmax]) for sliceNum in range(0, len(self.image_cube))])
            
            naive_sum_data()
            
            #These print statements are here for whenever you want to see if the inputs are actually updating when you click on the plots in spectrum
            #Can comment out if needed
            #print("backcoef: " + str(backcoef))
            print("xmin: " + str(xmin) + " xmax: " + str(xmax))
            print("ymin: " + str(ymin) + " ymax: " + str(ymax))
            print("z start: " + str(z_start) + " z end: " + str(z_end))
            print("z: " + str(z))
            return [[xmin, xmax], [ymin, ymax], [z_start, z_end], z, [], self.sumImageCube, self.TOF, self.E]
        except ValueError:
            print('One of your inputs is not a number')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ImageViewerWindow()
    w.setGeometry(100, 100, 800, 800)
    w.show()
    sys.exit(app.exec_())

import sys
from os import listdir
from os.path import isfile, join

from astropy.io import fits
import numpy as np

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *    

class selector(QRubberBand):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 4))
        color = QColor(Qt.green)
        #painter.setBrush(QBrush(color))
        #painter.setOpacity(0.3)
        painter.drawRect(event.rect())

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
        self.rect.setGeometry(QRect(top_left ,bottom_right))
 
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
    
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.viewer = image_viewer()
        self.files = None
        self.dir = "."

        #Load button
        self.load_button = QToolButton(self)
        self.load_button.setText('Select Directory')
        self.load_button.clicked.connect(self.load_dir)

        #Coordinates and their labels
        self.x_min_label = QLabel("X Min")
        self.x_min = QSpinBox()

        self.x_max_label = QLabel("X Max")
        self.x_max = QSpinBox()

        self.y_min_label = QLabel("Y Min")
        self.y_min = QSpinBox()

        self.y_max_label = QLabel("Y Max")
        self.y_max = QSpinBox()

        self.z_label = QLabel("Z")
        self.z = QSpinBox()
        self.z.setMinimum(0)
        self.z.valueChanged.connect(self.load_new_image_z)
        self.viewer.rect_sig.connect(self.update_xy)

        #Scroll bar
        self.scroll_bar = QScrollBar(self)
        self.scroll_bar.setOrientation(Qt.Horizontal)
        self.scroll_bar.setMinimum(0)
        self.scroll_bar.setMaximum(0)
        self.scroll_bar.valueChanged.connect(self.load_new_image_scroll_bar)
        
        #Add the image viewer and scroll bar
        layout = QHBoxLayout(self)
        VB = QVBoxLayout(self)
        VB.addWidget(self.viewer)
        VB.addWidget(self.scroll_bar)

        #Add the coordinates and the get file button
        HB = QVBoxLayout(self)
        HB.setAlignment(Qt.AlignLeft)
        HB.addWidget(self.load_button)

        HB.addWidget(self.x_min_label)
        HB.addWidget(self.x_min)

        HB.addWidget(self.x_max_label)
        HB.addWidget(self.x_max)
        
        HB.addWidget(self.y_min_label)
        HB.addWidget(self.y_min)
        
        HB.addWidget(self.y_max_label)
        HB.addWidget(self.y_max)

        HB.addWidget(self.z_label)
        HB.addWidget(self.z)

        layout.addLayout(VB)
        layout.addLayout(HB)

    def load_dir(self):
        self.dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if dir != '':
            self.files = listdir(self.dir)
            self.scroll_bar.setMaximum(len(self.files) - 1)
            self.z.setMaximum(len(self.files) - 1)
            self.load_new_image(0)

    # Loads a new image from the image library
    def load_new_image(self, value):
        if self.files != None:
            filename = self.dir + '/' + self.files[value]

            hdul = fits.open(filename)
            
            image_data = hdul[0].data
            image_data = image_data / image_data.max()
            image_data = image_data * 255
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
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setGeometry(500, 300, 800, 600)
    w.show()
    sys.exit(app.exec_())

# SSL-EAG-NeutronPy (v1.0)
Space Science Laboratory Experimental Astrophysics Group Neutron Imaging Data Visualization Tool at UC Berkeley for Fall 2020, Spring 2021, and Summer 2021.

## Project Overview
Element and/or isotope mapping is done using a neutron beam-line source and
neutron-counting microchannel plate detector with Timepix electronic readout. High-rate
simultaneous element-specific imaging creates a 10Gb data stream. Time at the testing site is
limited, with researchers often working around the clock to get their experiments done within a
reserved block of time. Given the time constraints, it's very useful to have a robust data
visualization software toolset so that the researcher can view data in near real-time to adjust
test parameters and optimize on the fly. The current project is a development effort for just such
a tool set. In addition, it is envisioned the toolset could be utilized from home or office. 

## Team
**PI**: Anton Tremsin (fa20, sp21, su21)

**Project Management**: Travis Curtis (fa20, sp21, su21), Nate Darling (fa20)

**Project Lead**: Yuki Ito (sp21, su21), Tino Trangia (sp21, su21), James Mang (fa20)

**Development Team**: Yuki Ito (fa20, sp21, su21), Tino Trangia (fa20, sp21, su21), Diether Delosreyes (fa20), and Paulina Umansky (fa20)

## Files
**Prototype**: Prototype the Development Team created during fa20 semester. Yuki Ito: spectrum.py, main.py; Tino Trangia: beamline.py; Diether Delosreyes: image_viewer.py; Paulina Umansky: materials.py

**NeutronPy v1.0**: The first edition of NeutronPy created and integrated by Yuki Ito and Tino Trangia for sp21 semester. More Information of how NeutronPy works can be found on the directory README and the code itself.

**NeutronPy Newest**: Our current updated iteration of NeutronPy working during the Summer 2021 timeline. An optimized version of 1.0. Added multi-threading functionalities to prevent the application from crashing on any arbitrary dataset (e.g. loading image cube and plotting / computation). Added new QOL such as loading bar.

## How To Launch
**1**. In your command line and in a directory you want NeutronPy to be in, you first want to clone this repository.  
```
git clone <insert URL here>
```
The URL should be located like so




![Capture](https://user-images.githubusercontent.com/45677734/120541452-c0185000-c39e-11eb-8495-a6cdb41f3a60.PNG)





 **2**. After cloning the repository, go to the version of NeutronPy you want to launch (preferably the newest and the most updated one) and make sure you have python 3.6 or recent installed in the command line and you will want to run ``` python main.py```. Note that you will most likely have to install some dependencies NeutronPy uses onto your device. It'll mention which dependencies you are currently missing from the error message when you try to run ```main.py```. Therefore, using a package management/ installment system like pip, you wuld want to install like so: ``` pip install <insert library or dependency name here> ```. Now you should be able to run ``` python main.py``` successfully! A window that looks something like this should pop up:
 
 
 
 ![Capture](https://user-images.githubusercontent.com/45677734/120541757-22715080-c39f-11eb-8383-82dd7689199c.PNG)
 
 


**3**. To use this toolset, you'd want a dataset of the neutron imaging sequence ready in a directory. Navigating yourself onto the "Select File / Directory", select the directory you want to view and work on and press Enter. It would take some time to load depending on the length of the data set and you should see the first slice of the imaging sequence on the GUI like so:


![Capture](https://user-images.githubusercontent.com/45677734/120542246-b93e0d00-c39f-11eb-9689-ab33c1d7ca91.PNG)



Now, you should be able to scroll through the sequence using the scrollbar right below the image and filling into the paramters you'd want to use, then upload those parameters for spectrum visualization by pressing the Plot 1 or Plot 2 buttons! Go crazy!

 **More information on how to debug and looking into the inner works, go to the README for the respective version**
 
## Logs

**Fall 2020**: With our initial development of this data visualization tool in mind, we decided to split up the software development into four parts: Spectrum visuzalier, materials parameter, image viewer (to view the fits data cube), and the beamline parameters. The semester throughout was mainly us figuring out PyQT and the QT framework and creating an initial UI for each of the components. Because of this, the integration process showed to be difficult as we had different implementation and coordination in mind and the semester ended with a basic integration scheme of these components.

**Spring 2021**: Given these scattered components, we decided to work on fully integrating these components to read off and save its parameter values and to be updated when visualizing in spectrum. We also created an updated GUI that is more user-friendly and do not suffer from errors with resizing. We ended the semester with being able to successfully extract information from the image viewer, material parameters, and the beamline parameters to be accessible and to be passed down as values for spectra visualization. Some pointers we want to address is that the loading of the fits files takes too long correlated with its size and the application sometimes crashes - need to develop some way to optimize memory allocation of these so-called "data cubes" of fits files.

**Summer 2021**: Given some of the bugs we found during spring such as application crashing and disk usage is enourmous for certain operations, Yuki ended up integrating multi-threading functionality so the application will not crash and set aside a separate thread to do most of its hard-computation / data loadout.

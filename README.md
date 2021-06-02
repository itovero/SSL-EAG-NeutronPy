# SSL-EAG-NeutronPy (v1.0)
Space Science Laboratory Experimental Astrophysics Group Neutron Imaging Data visualization Tool at UC Berkeley for Fall 2020, Spring 2021, and Summer 2021.

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

**Project Lead**: James Mang (fa20), Yuki Ito and Tino Trangia (sp21, su21)

**Development Team**: Yuki Ito (fa20, sp21, su21), Tino Trangia (fa20, sp21, su21), Diether Delosreyes (fa20), and Paulina Umansky (fa20)

## Files
**Prototype**: Prototype the Development Team created during fa20 semester. Yuki Ito: spectrum.py, main.py; Tino Trangia: beamline.py; Diether Delosreyes: image_viewer.py; Paulina Umansky: materials.py

**NeutronPy v1.0**: The first edition of NeutronPy created and integrated by Yuki Ito and Tino Trangia for sp21 semester. More Information of how NeutronPy works can be found on the directory README and the code itself.

**NeutronPy Newest**: Our current updated iteration of NeutronPy working during the Summer 2021 timeline. An optimized version of 1.0 

## How To Launch
**1**. In your command line and in a directory you want NeutronPy to be in, you first want to clone this repository.  
```
git clone <insert URL here>
```
The URL should be located like so
![Capture](https://user-images.githubusercontent.com/45677734/120540610-bcd09480-c39d-11eb-84b0-5f6ad6ce9cf7.PNG)


 **2**. After cloning the repository, go to the version of NeutronPy you want to launch (preferably the newest and the most updated one) and make sure you have python 3.6 or recent installed in the command line and you will want to run ``` python main.py```. Note that you will most likely have to install some dependencies NeutronPy uses onto your device. It'll mention which dependencies you are currently missing from the error message when you try to run ```main.py```. Therefore, using a package management/ installment system like pip, you wuld want to install like so: ``` pip install <insert library or dependency name here> ```. Now you should be able to run ``` python main.py``` successfully!
## Logs

**Fall 2020**: With our initial development of this data visualization tool in mind, we decided to split up the software development into four parts: Spectrum visuzalier, materials parameter, image viewer (to view the fits data cube), and the beamline parameters. The semester throughout was mainly us figuring out PyQT and the QT framework and creating an initial UI for each of the components. Because of this, the integration process showed to be difficult as we had different implementation and coordination in mind and the semester ended with a basic integration scheme of these components.

**Spring 2021**: Given these scattered components, we decided to work on fully integrating these components to read off and save its parameter values and to be updated when visualizing in spectrum. We also created an updated GUI that is more user-friendly and do not suffer from errors with resizing. We ended the semester with being able to successfully extract information from the image viewer, material parameters, and the beamline parameters to be accessible and to be passed down as values for spectra visualization. Some pointers we want to address is that the loading of the fits files takes too long correlated with its size and the application sometimes crashes - need to develop some way to optimize memory allocation of these so-called "data cubes" of fits files.

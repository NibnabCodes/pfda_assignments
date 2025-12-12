# Programming for Data Analytics - Winter 2025

![Alt text](images/data_analytics.png)  

## Overview 📊 

This repository contains four weekly task submissions completed as part of the assessment requirements for the Programming for Data Analytics at Atlantic Technological University – Galway.


## About this repository 📊 

This repository is comprised of the following files and folders:  

* An **assignments** folder containing jupyter notebooks & Python file for assignments:
  - assignment02-bankholidays.py  
  - assignment03-pie.ipynb  
  - assignment05-population.ipynb  
  - assignment_6_Weather.ipynb  
* A **data** folder containing a JSON dataset & CSV datasets used for the assignments.  
* An **image** folder that contains a .png file of the image used in this README,  
* A **.gitignore** file which contains all the files/folders to be ignored by Git in this repository.
* A **README** file that contains the utility of each program, list of dependencies, how to: set up environment, download the repository & run the code.  
* A **requirements.txt** file containing all the Python packages that the programs depend on & their versions.


## Dependencies 📊 

* Python==3.12.1  
* Matplotlib.pyplot==3.10.7
* numpy==2.3.4
* pandas==2.3.3
* json = built in, no version
* seaborn==0.13.2

## Environment Setup 📊 

**Git**  
Download the latest version of Git at:  
https://git-scm.com/downloads

**GitHub**  
Create a free GitHub account at:  
https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home

**Anaconda**  
I would recommend using Anaconda as it comes bundled with Python==3.12.7 & the Python libraries necessary to run the code in this repository.  
Install Anaconda using the following steps:  
1. Download Anaconda from:  
https://www.anaconda.com/download
2. Open the downloaded file & press next, next
3. When the advanced options appear check the following boxes:  
  - Add to PATH environment variable  
  - Make this version your default Python

**Visual Studio Code**
Download Visual Studio Code at:  
https://code.visualstudio.com/Download

## How to Download Repository 📊 


You can clone this repository to VS Code using the following steps:
1. Copy the repositories URL:  
https://github.com/NibnabCodes/pfda_assignments.git 
2. Create a folder in VS Code of where you want to store the cloned repository
3. Open new terminal in VS Code & input following:  
  - git clone PASTED.URL - To clone repository  
  - git config pull.rebase false - Set pull mode to merge  
  - git pull - To pull the content of the repository  

The repository should now be accessible in VS Code & ready to execute.

## How to Run the Code 📊 

To run the code in VS Code follow these steps:  

1. Open Terminal & input the following commands:  
2. cd followed by the folder that the repository is stored in.
3. cd pfda_assignments - To access repository  
4. cd to assignments folder  
  - To run .py file, input *python assignment02-bankholidays.py* into the terminal
  - To run jupyter notebooks:  
    - Open .ipynb file
    - In the top right-hand corner click "select kernel"
    - select Python environment
    - To execute the cells to run the code within the notebook, select "Run All" or run the cells one by one by clicking "▶️ Execute cell" on the top left-hand corner of the cell
* To move between folders in the repository:  
  - cd .. - To go up one directory. - Each .. moves you up one directory
  - cd ..//.. - To go up two directories  

## References 📊 

Please see assignments for references used.
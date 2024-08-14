# Introduction 
This project automatically tests the GET requests on the Swagger API website

Use the folder called "ManyBuild POST"

Folder "POST" is outdated

# problem TO-DO:
I can't seem to get the VScode to work in Git with the YAML even though it is the same code

# Prerequisites

**Running this requires pip / python:**
https://www.python.org/downloads/

You need to download selenium for you version of chrome or edge.

For example if your chrome version is 126.xx.xx you need to download the matching version of the webdrivers. 

**Link for downloading selenium:**
https://pypi.org/project/selenium/

(keep in mind I am using python)

**Link for downloading chromedriver:**
https://googlechromelabs.github.io/chrome-for-testing/

(Again get the version that matches your chrome)

# How to Run

**1. Command Line**

> [!IMPORTANT]

> You will need to change a few pieces of code.

In the file called "newFileOpen" you must redirect the path to your downloads

```
#lines 7 - 9 in newFileOpen.py
def openNewFile():
    # Specify the directory where your downloads are saved
    download_dir = r'c:/Users/HDouglas/Downloads'  # Replace with your actual download directory c:\Users\HDouglas\Downloads / c:/Users/hayde/Downloads
```
Replace r'c:/Users/HDouglas/Downloads' with your own local downlaod directory

You will also need to change the line of code in "masterFile.py" (line 35) to where your chrome driver is downloaded
```
chrome_driver_path = r'C:/webdrivers/chromedriver.exe'  # Adjust the path as necessary
```

Once these steps are done you should be able to open cmd line and run the following command
```
cd whereFileIsLocated
python masterFile.py
```

**2. VS Code**

Open folder with all files -> open masterFile -> Select Run


# NOTE
> You need to have all files downloaded and in a file to run

# Global Variables
There is a file named globalVars in both the GET and the POST folders. 

This is an important file. Any call that takes an input, the data comes from this file. 

Feel free to check it out and replace it's data with new data for better testing.

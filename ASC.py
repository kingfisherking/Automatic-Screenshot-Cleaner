#importing os to access filenames and paths
#importing shutil to more easily move files, os module doesn't have great file moving functions
import os
import shutil
#accessing user's desktop, this currently assumes the program is deployed in a folder on the desktop
CWD = os.getcwd()
desktopPath = CWD[0:CWD.find("Desktop")+7]+"\\" #+7 for the length of 'Desktop/' to include in the path

# searching desktop for folder labeled "Screenshots", creating one if it doesn't exist
#this variable essentially names the folder, change the word "Screenshots" to what you want
screenshotPath = desktopPath+'Screenshots' 
print(os.path.exists(screenshotPath))
if os.path.exists(screenshotPath) != True:
    os.makedirs(screenshotPath) #creates a folder on desktop named after that variable

#creating a list of strings containing the filenames for all files in desktop
fileList = os.listdir(desktopPath)

for file in fileList:
    if "Screen Shot" in file: #this is how screenshots are created in Mac, will have to fiddle with this
        if file.endswith(".png") or file.endswith(".jpg"):
            print(desktopPath+file)
            shutil.move(desktopPath+file, screenshotPath) #moves files from desktop to screenshot folder

#devlog 9/30: right now, this program fails if there's a screenshot with the same name in that folder already
#not tpically a problem, but testing is difficult and surely there's a case

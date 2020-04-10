import pyautogui
pyautogui.FAILSAFE=True

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":'''Roy Rodgers, Health Insurance, Hair, Laundry, Dog Food''',"limit":25, "size":">640*480", "print_urls":True}   #creating list of arguments
#paths = response.download(arguments)   #passing the arguments to the function
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
from urllib.request import urlopen

import os.path

from os import walk

import os




all_folders = os.path.join("downloads")




folders = []
for (dirpath, dirnames, filenames) in walk(all_folders):
    folders.extend(dirnames)
    break



def createImage(file, data_folder):
    
    file_to_open = os.path.join(data_folder, file)
    img = Image.open(file_to_open)
    img = img.convert("RGBA")

    #resize
    #header 1200x7500
    img= img.resize((1200,750))

    # Remove alpha for saving in jpg format.
    img = img.convert("RGB") 
    img.save(file_to_open)
    img.show()

fileID=0
folderID=0

try:
    while True:
        while (folders[folderID] != None):
            data_folder=os.path.join("downloads",folders[folderID])
            print (data_folder)
            f = []
            for (dirpath, dirnames, filenames) in walk(data_folder):
                f.extend(filenames)
                break
            print (f[0])
            try:
                while (f[fileID]!= None):
                    try:
                        createImage(f[fileID],data_folder)
                    except ValueError:
                        print ("Value Error")
                    except OSError:
                        print ("OS error")
                    fileID=fileID+1
                                        
            except IndexError:
                print("next up?")
                fileID=0
            folderID=folderID+1
except KeyboardInterrupt:
    pass

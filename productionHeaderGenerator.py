from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
from urllib.request import urlopen

import os.path

from os import walk

import os

#for failsafe
import pyautogui
pyautogui.FAILSAFE=True


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
    img= img.resize((1200,750))


    #bg fill is (R,G,B, opacity)
    tmp = Image.new('RGBA', img.size, (0,0,0,0))
    draw = ImageDraw.Draw(tmp)
    draw.rectangle(((0, 0), (1200, 750)), fill=(13,71,161,157))

    # Alpha composite the two images together.
    img = Image.alpha_composite(img, tmp)
    txt = Image.new('RGBA', img.size, (255,255,255,0))


  # Create Text
    fontPackage = os.path.join("Roboto-Regular.ttf")
    fontPackage = os.path.join("Roboto-Regular.ttf")
    fontSize=90
    fontSize2=50
    img = Image.alpha_composite(img, txt)
    
    # Create Text
    
    fnt = ImageFont.truetype(fontPackage, fontSize)
    d = ImageDraw.Draw(txt)
    d.text((100,160), folders[folderID],  font=fnt, fill=(251,192,45,255))
    d.text((200,300), "Calories and Protein", font=fnt, fill=(251,192,45,255))
    d.text((700,430), "Per Dollar", font=fnt, fill=(251,192,45,255))

    fnt2 = ImageFont.truetype(fontPackage, fontSize2)
    d.text((100,60), "Efficiency Is Everything Presents",  font=fnt2, fill=(251,192,45,255))
  
    
    img = Image.alpha_composite(img, txt)

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
                    fileID=fileID+1
                                        
            except IndexError:
                print("next up?")
                fileID=0
            folderID=folderID+1
except KeyboardInterrupt:
    pass

## script to resize images for the thumbnails of the Image Library
import os
from PIL import Image


fileList = []
for file in os.listdir():
    fileList.append(file)

fileList.remove("resizer.py")
    
for filePath in fileList:
    image = Image.open(filePath)
    image = image.resize((24, 24), Image.NEAREST)
    image.save(filePath)

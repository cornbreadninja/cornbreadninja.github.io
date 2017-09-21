import PIL
import os
from PIL import Image


all_files = os.listdir(os.getcwd())

for file in all_files:
   if file[-3:] == "jpg":
       img = Image.open(file)
       img = img.resize((1920,1080), PIL.Image.ANTIALIAS)
       img.save('resized\\%s' % file)
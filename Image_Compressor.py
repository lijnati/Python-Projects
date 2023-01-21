#first install Pillow package : pip install Pillow

import PIL
from PIL import Image
from tkinter.filedialog import *

file_path=askopenfilename()
img=PIL.Image.open(file_path)
myHeight,myWidth=img.size

img=img.resize((myHeight,myWidth),PIL.Image.ANTIALIAS)
save_path=askopenfilename()
img.save(save_path+"compressed.jpg")

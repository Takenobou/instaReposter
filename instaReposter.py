import os
import time
import picGrab
import autopost
import platform
from multiprocessing import Process

def ensure_dir():
    dir = os.getcwd()
    if platform.system() == 'Linux':
        ImagePath = dir + "/Images"
        IndexFile = dir + "/lastimageindex.txt"
    elif platform.system() == 'Windows':
        ImagePath = dir + "\\Images"
        IndexFile = dir + "\\lastimageindex.txt"

    if not os.path.isdir(ImagePath):
        print("Creating image folder")
        os.makedirs(ImagePath)
    if not os.path.exists(IndexFile):
        with open(IndexFile, 'w') as f:
            f.write("URL Codes for Images") 

def multiProcessor(processMode):
    if processMode == 1:
        Process(target=InstaPoster).start()
        #InstaPoster()
    elif processMode == 2:
        Process(target=RedditImageGrab).start()
        #RedditImageGrab()

# Instagram poster script
def InstaPoster():
        print("Posting Initiated")
        autopost.main()

#Image grabber and file sorter
def RedditImageGrab():
    print('Image folder is empty, repopulating now')
    picGrab.main()     
    print("Image folder repopulated")      

#multiprocessing the functions
if __name__ == '__main__':
        ensure_dir()
        multiProcessor(1)
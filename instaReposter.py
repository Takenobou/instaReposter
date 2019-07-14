import os
import sys
import time
import picGrab
import autopost
from multiprocessing import Process

d = os.getcwd()
ImagePath = d + "\\Images"
def ensure_dir():
        if not os.path.isdir(ImagePath):
                print("Creating image folder")
                os.makedirs(ImagePath)

# Instagram poster script
def InstaPoster():
        print("Posting Initiated")
        autopost.main()


#Image grabber and file sorter
def RedditImageGrab():
    while True:
        dirContents = os.listdir(ImagePath)
        if len(dirContents) == 0:
            print('Image folder is empty')
            print("Repopulating now")
            picGrab.main()       
        

#multiprocessing the functions
if __name__ == '__main__':
        ensure_dir()
        Process(target=RedditImageGrab).start()
        Process(target=InstaPoster).start()
        
import os
import sys
import time
import picGrab
import autopost
from multiprocessing import Process

dir = os.getcwd()
ImagePath = dir + "\\Images"
def ensure_dir():
        if not os.path.isdir(ImagePath):
                print("Creating image folder")
                os.makedirs(ImagePath)


def multiProcessor( processMode ):

    if processMode == 1:
        Process(target=InstaPoster).start()
    elif processMode == 2:
        Process(target=RedditImageGrab).start()


# Instagram poster script
def InstaPoster():
        print("Posting Initiated")
        autopost.main()


#Image grabber and file sorter
def RedditImageGrab():
    #while True:
        #dirContents = os.listdir(ImagePath)
        #if len(dirContents) == 0:
    print('Image folder is empty, repopulating now')
    #start_time = time.time()
    picGrab.main()
    #elapsed_time = time.time() - start_time      
    print("Image folder repopulated")
    #print("The update took " + str(elapsed_time) + "s")
    

        

#multiprocessing the functions
if __name__ == '__main__':
        ensure_dir()
        multiProcessor(1)
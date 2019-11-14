import os
import time
import picGrab
import autoPost
import platform
from os import listdir
from random import randint
from os.path import isfile, join
from multiprocessing import Process

def main():
    #setting up directories
    dir = os.getcwd()
    print("Checking platform...")
    if platform.system() == 'Linux':
        ImagePath = dir + "/Images"
        IndexPath= dir + "/lastimageindex.txt"
        clear = lambda: os.system('clear')
    elif platform.system() == 'Windows':
        clear = lambda: os.system('cls')
        ImagePath = dir + "\\Images"
        IndexPath = dir + "\\lastimageindex.txt"

    #creating directories if not found
    print("Checking directories...")
    if not os.path.isdir(ImagePath):
        print("Creating image folder...")
        os.makedirs(ImagePath)
    if not os.path.exists(IndexPath):
        print("Creating indexing file...")
        with open(IndexPath, 'w') as f:
            f.write("URL Codes for Images \n")
    
    hashtags = "#meme #memes #dankmemes #funny #funnymemes #memesdaily #lol #edgymemes #dank #offensivememes #lmao #follow #like #bhfyp #humor #dankmeme #reddit #edgy #comedy #fun #instagram #cringe #offensive #sad #memestagram"
    TargetSub = 'memes'
    grabAmount = 6

    while True:
        os.chdir(ImagePath)
        ListFiles = sorted([f for f in listdir(ImagePath) if isfile(join(ImagePath, f))])
        print(ListFiles)
        print("Total number of photos in this folder:" + str(len(ListFiles)))  
        
        if len(listdir(ImagePath)) != 0:
            #post image
            for i, _ in enumerate(ListFiles):
                photo = ListFiles[i]
                print("----------------------------------------------------------")
                print("Progress: " + str([i + 1]) + " of " + str(len(ListFiles)))
                credit = os.path.splitext(photo)[0]
                igCaption = ("Originally posted by: /u/" + credit + " on Reddit" ".\n.\n.\n.\n.\n.\n.\n.\nTags:\n\n" + hashtags)
                Process(target=autoPost.main(photo, igCaption)).start()
                os.remove(photo)

                #timer start
                clear() 
                n = randint(2400, 3600)
                print("----------------------------------------------------------")  
                for remaining in range(n, 0, -1):
                    print("{:2d} seconds remaining to next upload.".format(remaining))
                    upLine = '\x1b[1A'
                    delLine = '\x1b[2K'
                    time.sleep(1)
                    print(upLine + delLine + upLine)
        elif len(listdir(ImagePath)) == 0:
            #image grab
            Process(target=picGrab.main(grabAmount, ImagePath, IndexPath, TargetSub)).start()
            if len(listdir(ImagePath)) != grabAmount:
                time.sleep(5)

if __name__ == "__main__":
    print("instaReposter")
    main()
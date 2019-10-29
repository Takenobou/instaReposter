import os
import sys
import time
import platform
import instaReposter
from PIL import Image
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

d = os.getcwd()
if platform.system() == 'Linux':
    slash = '/'
elif platform.system() == 'Windows':
    slash = '\\'

ImagePath = d + slash + "Images"
hashtags = "#meme #memes #dankmemes #funny #funnymemes #memesdaily #lol #edgymemes #dank #offensivememes #lmao #follow #like #bhfyp #humor #dankmeme #reddit #edgy #comedy #fun #instagram #cringe #offensive #sad #memestagram"

def main():  
        postIt()

def instaLogin():
        #os.chdir("..")
        f = open("instaLogin.txt", "r")
        igUser = f.readline()
        igPassword = f.readline()
        f.close()
        igapi = InstagramAPI(igUser, igPassword)
        igapi.login()  # login
        os.chdir(ImagePath)
        return igapi

def postIt():
        igapi = instaLogin()
        try:
                while True:
                        os.chdir(ImagePath)
                        ListFiles = sorted([f for f in listdir(ImagePath) if isfile(join(ImagePath, f))])
                        print(ListFiles)
                        print("Total number of photos in this folder:" + str(len(ListFiles)))  
        
                        if len(listdir(ImagePath)) != 0:
                                for i, _ in enumerate(ListFiles):
                                        photo = ListFiles[i]
                                        print("----------------------------------------------------------")
                                        print("Progress: " + str([i + 1]) + " of " + str(len(ListFiles)))
                                        credit = os.path.splitext(photo)[0]
                                        IGCaption = ("Originally posted by: /u/" + credit + " on Reddit" ".\n.\n.\n.\n.\n.\n.\n.\nTags:\n\n" + hashtags)
                                        print("Now uploading this photo to Instagram: " + photo)
                                        image = Image.open(photo)
                                        image.save(photo)
                                        igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
                                        print("Upload Successful")
                                        os.remove(photo)
                                        timer()
                        elif len(listdir(ImagePath)) == 0:
                                #image grab
                                instaReposter.multiProcessor(2)
                                time.sleep(10)
                                       
        except KeyboardInterrupt:
                print("\nProgram interrupted")
                pass            

def timer():
        #comment for debugging
        if platform.system() == 'Linux':
            clear = lambda: os.system('clear')
        elif platform.system() == 'Windows':
            clear = lambda: os.system('cls')
        clear() 
        n = randint(2400, 3600)
        print("----------------------------------------------------------")  
        for remaining in range(n, 0, -1):
                print("{:2d} seconds remaining to next upload.".format(remaining))
                CURSOR_UP_ONE = '\x1b[1A'
                ERASE_LINE = '\x1b[2K'
                time.sleep(1)
                print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
        

if __name__ == "__main__":
    print ("Autopost imported")

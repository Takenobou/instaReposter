import os
import sys
import time
import instaReposter
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

d = os.getcwd()
ImagePath = d + "\\Images"
hashtags = "#meme #memes #dankmemes #funny #funnymemes #memesdaily #lol #edgymemes #dank #offensivememes #lmao #follow #like #bhfyp #humor #dankmeme #reddit #edgy #comedy #fun #instagram #cringe #offensive #sad #memestagram"

def main():  
        os.chdir(ImagePath)
        ListFiles = sorted([f for f in listdir(ImagePath) if isfile(join(ImagePath, f))])
        print(ListFiles)
        print("Total number of photos in this folder:" + str(len(ListFiles)))
        postIt()


def instaLogin():

        os.chdir("..")
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
                                        igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
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

    n = randint(1800, 3600)
    for remaining in range(n, 0, -1):
        print("----------------------------------------------------------")
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining to next upload.".format(remaining))
        sys.stdout.flush()

        time.sleep(1)
        #comment for debugging
        clear = lambda: os.system('cls')
        clear() 
        


if __name__ == "__main__":
    print ("Autopost imported")

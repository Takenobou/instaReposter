import os
import sys
import time
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

d = os.getcwd()
ImagePath = d + "\\Images"

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
        print("Logged in")
        os.chdir(ImagePath)
        return igapi


def postIt():
        igapi = instaLogin()
        os.chdir(ImagePath)
        ListFiles = sorted([f for f in listdir(ImagePath) if isfile(join(ImagePath, f))])
        print(ListFiles)
        print("Total number of photos in this folder:" + str(len(ListFiles)))
        for i, _ in enumerate(ListFiles):
                photo = ListFiles[i]
                print("----------------------------------------------------------")
                print("Progress: " + str([i + 1]) + " of " + str(len(ListFiles)))
                credit = os.path.splitext(photo)[0]
                IGCaption = ("Originally posted by: /u/" + credit + " on Reddit" ".\n.\n.\n.\n.\n.\n.\n.\nTags:\n\n#meme #memes #dankmemes #funny #funnymemes #memesdaily #lol #edgymemes #dank #offensivememes #lmao #follow #like #bhfyp #humor #dankmeme #edgy #comedy #fun #instagram #cringe #offensive #sad #memestagram")
                print("Now uploading this photo to Instagram: " + photo)
                igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
                os.remove(photo)
                timer()


def timer():
    n = randint(1400, 1800)
    print("----------------------------------------------------------")
    for remaining in range(n, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining to next upload.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
        clear = lambda: os.system('cls')
        clear()


if __name__ == "__main__":
    print ("autopost imported")

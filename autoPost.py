import os
from InstagramAPI import InstagramAPI

def main(photo, igCaption):
    dir = os.getcwd()
    
    #read login file
    os.chdir("..")
    with open("instaLogin.txt", 'r') as f: 
        igUser = f.readline()
        igPassword = f.readline()
    igapi = InstagramAPI(igUser, igPassword)
    igapi.login() #login
    
    #start uploading
    os.chdir(dir)
    print("----------------------------------------------------------")
    print("Now uploading this photo to Instagram: " + photo)
    igapi.uploadPhoto(photo, caption=igCaption, upload_id=None)
    print("Upload Successful")
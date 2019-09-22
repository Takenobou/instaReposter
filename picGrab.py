import os
import PIL
import praw
import requests
from PIL import Image

#reddit image grabber, resizer and downloader



def main():
        clID = ""
        clSE = ""
        User = ""
        Password = ""
        reddit = praw.Reddit(client_id= clID, 
        client_secret = clSE,
        username = User,
        password = Password,
        user_agent = 'picGrabV1')

        
        subreddit = reddit.subreddit('memes') #target subreddit
        d = os.getcwd()
        ImagePath = d + "\\Images" #image path
        hot_python = subreddit.hot(limit= 8) #amount of images to be downloaded (limit + 1 stickie)

        for submission in hot_python:
            if not submission.stickied and not submission.over_18:
                print (submission.author)
                print (submission.url)
                print (hot_python)
                submission.upvote()
                imageName = str(submission.author)
                print (imageName)
                img_data = requests.get(submission.url).content
                with open(ImagePath + "\\" + imageName + '.jpg', 'wb') as handler: #writing the image
                    handler.write(img_data)
                
                #resizing the image for instagram

                with Image.open(ImagePath + "\\" + imageName + '.jpg') as img:
                    width, height = img.size
                if  width > 1920 or height > 1080:
                    baseheight = 1080
                    img = Image.open(ImagePath + "\\" + imageName + '.jpg')
                    hpercent = (baseheight / float(img.size[1]))
                    wsize = int((float(img.size[0]) * float(hpercent)))
                    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
                    img.save(ImagePath + "\\" + imageName+ '.jpg')
                    
                    

if __name__ == "__main__":
    print("PicGrab imported")

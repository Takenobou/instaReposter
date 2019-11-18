import os
import PIL
import praw
import mmap
import platform
import requests
from PIL import Image

if platform.system() == 'Linux':
    slash = '/'
elif platform.system() == 'Windows':
    slash = '\\'

#reddit image grabber and prepper
def main(grabAmount, ImagePath, IndexPath, TargetSub):
    clID = ""
    clSE = ""
    User = ""
    Password = ""
    reddit = praw.Reddit(client_id= clID, 
    client_secret = clSE,
    username = User,
    password = Password,
    user_agent = 'picGrabV1')

    subreddit = reddit.subreddit(TargetSub) #target subreddit
    ImagePath = os.getcwd()
    IndexPath = ".." +slash+ "lastimageindex.txt"
    hot_python = subreddit.hot(limit= grabAmount) #amount of images to be downloaded (check for sticky posts)

    for submission in hot_python:
        if not submission.stickied and not submission.over_18:
            url = submission.url
            submission.upvote()
            imageName = str(submission.author)
            print (imageName)
            #getting post url code for lastimageindex.txt
            img_data = requests.get(url).content
            url = url[18:]
            url = url[:-4] 
            burl = str.encode(url)
         
#checking if the image has been posted before
            #reading
            with open(IndexPath, "rb", 0) as file, \
                mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
                if s.find(burl) != -1:
                    print('Image already posted')
                else:
                    print('New Image')
                    with open(ImagePath + slash + imageName + '.jpg', 'wb') as handler: #writing the image
                        handler.write(img_data)

                    #prepping the image for instagram
                    with Image.open(ImagePath + slash + imageName + '.jpg') as img:
                        Oimg_w, Oimg_h = img.size # original image dimensions
                        imgRatio = Oimg_w / Oimg_h #rough ratio
                        if  imgRatio < 1 :
                            #portrait
                            imagePrep(1, imageName, Oimg_h, ImagePath)
                        elif imgRatio > 1:
                            #Landscape
                            imagePrep(2, imageName, Oimg_h, ImagePath)
                        elif imgRatio == 1:
                            #Square
                            imagePrep(3, imageName, Oimg_h, ImagePath)
                        
                        #removing EXIF data
                        image = Image.open(ImagePath + slash + imageName + '.jpg')
                        image.save(ImagePath + slash + imageName + '.jpg')
                        
                    #appending
                    with open(IndexPath, "a") as file:      
                        file.write(url + "\n")
        
def imagePrep(imageType, imageName, Oimg_h, ImagePath):
    if imageType == 1:
        baseheight = int(Oimg_h)
        backwidth = int((Oimg_h/5)*4)
    elif imageType == 2:
        baseheight = int(Oimg_h)
        backwidth = int(Oimg_h*1.91)
    elif imageType == 3:
        baseheight = int(Oimg_h)
        backwidth = int(Oimg_h)
    
    #resizing
    img = Image.open(ImagePath + slash + imageName + '.jpg')
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
                    
    #making a white background
    img_w, img_h = img.size
    background = Image.new('RGB', (backwidth, baseheight), color = 'white')
    bg_w, bg_h = background.size
    offset=((bg_w-img_w)//2,(bg_h-img_h)//2)

    #composing final image
    background.paste(img, offset)
    background.save(ImagePath + slash + imageName + '.jpg')

if __name__ == "__main__":
    print("PicGrab imported")

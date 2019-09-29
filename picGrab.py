import os
import PIL
import praw
import mmap
import requests
from PIL import Image

#reddit image grabber and prepper


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
        ImagePath = os.getcwd()
        #ImagePath = d + "\\Images" #image path
        hot_python = subreddit.hot(limit= 8) #amount of images to be downloaded (limit + 1 sticky)

        with open("C:\\Users\\alexm\\Documents\\AutoInsta\\lastimageindex.txt", "a") as file:      
            file.write("\n\n")
        

        for submission in hot_python:
            if not submission.stickied and not submission.over_18:
                url = submission.url
                print (url)
                submission.upvote()
                imageName = str(submission.author)
                print (imageName)
                img_data = requests.get(url).content
         
#checking if the image has been posted before
                
                url = url[18:]
                url = url[:-4] 

                burl = str.encode(url)
                #reading
                with open("..\\lastimageindex.txt", "rb", 0) as file, \
                    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
                    if s.find(burl) != -1:
                        print('Image already posted')
                        newImage = False
                    else:
                        print('New Image')
                        newImage = True
                        with open(ImagePath + "\\" + imageName + '.jpg', 'wb') as handler: #writing the image
                            handler.write(img_data)


                        #prepping the image for instagram


                        with Image.open(ImagePath + "\\" + imageName + '.jpg') as img:
                            Oimg_w, Oimg_h = img.size # original image dimensions
                        if  Oimg_w > 1080 or Oimg_h > 1350:
                    
                            #resizing
                            baseheight = 1350
                            img = Image.open(ImagePath + "\\" + imageName + '.jpg')
                            hpercent = (baseheight / float(img.size[1]))
                            wsize = int((float(img.size[0]) * float(hpercent)))
                            img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
                    
                            #making a white background
                            img_w, img_h = img.size
                            background = Image.new('RGB', (1080, 1350), color = 'white')
                            bg_w, bg_h = background.size
                            offset=((bg_w-img_w)//2,(bg_h-img_h)//2)

                            #composing final image
                            background.paste(img, offset)
                            background.save(ImagePath + "\\" + imageName + '.jpg')
                #appending
                if newImage == True:
                    with open("..\\lastimageindex.txt", "a") as file:      
                        file.write(url + "\n")
        
        # delete old values
        with open("..\\lastimageindex.txt", 'rt') as lines:
            # while the line is not empty drop it
            for line in lines:
                if not line.strip():
                    break
        
            with open("..\\lastimageindex.txt", 'wt') as out:
                out.writelines(lines)


                 
                






if __name__ == "__main__":
    print("PicGrab imported")

# instaReposter

## Dead, Instagram has closed the endpoint for uploading images to the public so this won't work. 

### Support for Linux and Windows

A bot that grabs the hottest images from reddit (default is r/memes) and reposts them to instagram (in a random 30-60min interval)

### **Pre-Requesites:**

- An Instagram account
- A Reddit account with an [app](https://old.reddit.com/prefs/apps/) created 
- Python 3


### **Instructions:**

#### 1. Use Pip to install the required packages

  ##### ***Recommended:***

  `pip install -r requirements.txt`

  ##### **Manual:**

   PRAW ([Reddit API](https://github.com/praw-dev/praw)):
    `pip install praw`

   InstagramAPI ([Instagram API](https://github.com/LevPasha/Instagram-API-python)):
    `pip install InstagramAPI`

   pillow (PIL)
    `pip install pillow`

#### 2. Login
  - In instaLogin.txt change Username to your Instagram username and Password to your Instagram password
  - In picGrab.py change clID to your app client ID, clSE to your client Secret,
    change user to your Reddit username and password to your Reddit password

#### 3. Run instaReposter.py

  - Navigate to the directory in the terminal
    run: `python instaReposter.py`

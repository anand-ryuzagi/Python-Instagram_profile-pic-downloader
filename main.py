import requests
import json
import shutil
import os

userID = input("Enter Instagram user Id = ")
head = "https://instagram.com/"+ userID
tail = "/?__a=1"
user_agent = {'User-agent': 'Mozilla/5.0'}
url = head + tail

response = requests.get(url, headers = user_agent).json()

dp_location = response["graphql"]["user"]["profile_pic_url"]
hd_dp_location = response["graphql"]["user"]["profile_pic_url_hd"]

profile_pic = requests.get(hd_dp_location, stream = True)

with open("C:\\Users\\user\\Desktop\\practice\\New folder\\Python Insta profile pic downloader\\img.jpg","wb") as f:
    shutil.copyfileobj(profile_pic.raw,f)
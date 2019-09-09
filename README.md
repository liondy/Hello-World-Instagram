# Hello-World-Instagram
Posting a photo using python

Step 1: Using the majek word import:

Installation: Open the terminal

sudo pip3 install instapy-cli .<br>
Step 2: Create a python file
.

from instapy_cli import client 
username = 'michaelliondy' # your username 
password = '**********' # your password

image = 'hello.jpg' --> here you can put the image directory or name better to have it in the same folder as your python file.

text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags like #pythoncode #webdeveloper ' 
with client(username, password) as cli: 
cli.upload(image, text) .<br>
Step 3: Run the code and check your Instagram account

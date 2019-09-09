# Hello-World-Instagram
Posting a photo using python. You need to have python2 / python3. Here is a complete guide in Ubuntu Linux 18.04 for uploading your photo via python

## Step 1: Installation

Open the terminal

For python2 <br>
`sudo pip install instapy-cli` <br>


For python3 <br>
`sudo pip3 install instapy-cli` <br>

## Step 2: Create a python file

    from instapy_cli import client 
    username = 'michaelliondy' # your username 
    password = '**********' # your password
    
    image = 'hello.jpg' --> here you can put the image directory or name better to have it in the same folder as your python file.

    text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags like #pythoncode #webdeveloper ' 
    with client(username, password) as cli: 
    cli.upload(image, text) .<br>
    
## Step 3: Run the code and check your Instagram account

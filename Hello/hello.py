from instapy_cli import client
username = 'michaelliondy' #your username
password = '************' #your password

image = 'hello.jpg'
text = "You don't know how much could be done using python.\n This is a try for posting an Instagram post using python.\n This method was taken from @python.learning.\n Source code on my github: #python3 #beginner #cupu"

with client(username,password) as cli:cli.upload(image,text)
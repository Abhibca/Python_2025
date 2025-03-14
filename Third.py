import os

#select the directory whose  content you want to list
directory_path = '/'

#Use the os module to list the diretory content
contents = os.listdir(directory_path)

#print the content of the directory
for item in contents:
    print(item)
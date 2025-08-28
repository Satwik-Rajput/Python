import os

# Speciifie =the directory you want to list
directory_path = '/KMPlayer'

#List all files and directory in the specified path 
contents = os.listdir(directory_path)

#Print each file and directory name
for file in contents:
    print(file)

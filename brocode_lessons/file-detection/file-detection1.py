# relative file path: folder/test.txt
# absolute file path = C:/Users/Matthew/Desktop/test.txt

import os

file_path = "file-detection/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
        
else:
    print("That location doesn't exist")
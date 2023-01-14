import os,shutil
from pathlib import Path
str1=input("enter the extension to be searched:")
for folder,subfolder,file in os.walk('/home/aniketh/Desktop/Automate_the_boring_stuff/Chapter10/Selective_Search'):
    for files in file:
        if files.endswith(str1):
            shutil.copy(os.path.join(folder, files),'/home/aniketh/Desktop/Automate_the_boring_stuff/Chapter10/newfolder')
        else:
            print("no file")
        

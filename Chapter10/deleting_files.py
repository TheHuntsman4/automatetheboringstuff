import os
for folder,subfolder,files in os.walk('/home/aniketh/Desktop/newfolder'):
    for file in files:
        path=os.path.join(folder,file)
        if os.path.getsize(path)>100000000:
            print("deleting file :",os.path.abspath(path))
            os.unlink(path)



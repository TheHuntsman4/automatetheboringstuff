import re,shutil,os
prefix=input("enter the prefix:")
filename_regex=re.compile(r'^%s(\d)(\d)(\d).txt$'%prefix)
os.chdir('/home/aniketh/Desktop/foo')
i=0
for folder ,subfolder,files in os.walk('/home/aniketh/Desktop/foo'):
    for file in files:
        file_name=os.path.basename(file)
        reg_file=filename_regex.search(file)
        number=reg_file.group(1)
        n=int(number)
        if n!=i:
            n=i
            file_name_new=prefix+"00"+str(i)+'.txt'
            shutil.move(file,file_name_new)
            print("changing",file_name,"to",file_name_new)
            i+=1
        else:
            i+=1
            print("no change")
            

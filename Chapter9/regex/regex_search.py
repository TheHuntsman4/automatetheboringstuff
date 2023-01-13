import os,re
exp=input("enter search")
regex=re.compile(exp)

cd=os.listdir('./')

txt_files=[]
for file in cd:
    if file.endswith('.txt'):
        txt_files.append(file)
for file in txt_files:
    current=open(file)
    current_content=current.readlines()
    current.close()
    for line in current_content:
        search=regex.findall(line)
        if search is not None:
            for i in search:
                print(search)
        else:
            print("no matches")

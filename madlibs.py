import re

file=open('madlibs.txt')
text=file.read()
file.close()

madlibs=re.compile(r'(NOUN)|(ADJECTIVE)|(VERB)')
for i in madlibs.findall(text):
    for j in i:
        str1=input("enter a %s" %j)
        text=re.sub(j,str1)
print(text)
file=open('madlibs.txt','w')
file.write(text)
file.close()

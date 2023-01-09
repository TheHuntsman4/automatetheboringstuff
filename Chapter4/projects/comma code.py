import sys
def comma(spam):
    out=''
    #spam.insert(-1,'and')
    for i in range(0,len(spam)-1):
        out+=spam[i]+', '
    out+='and '+spam[-1]
    print(out)
    sys.exit
spam=[] 
l=int(input("enter size of list:"))
if l==0:
    print("error")
else:
    for i in range(0,l):
        a=input()
        spam.append(a)
    comma(spam)

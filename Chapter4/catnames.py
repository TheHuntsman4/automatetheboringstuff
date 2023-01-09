catnames=[]
while True:
    print("enter the name of cat"+str(len(catnames)+1),"(or enter nothing to stop:)")
    name=input()
    if name=='':
        break
    catnames=catnames+[name]
print("the cats names are :")
for i in catnames:
    print(' '+ i)

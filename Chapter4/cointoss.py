import random
for
count=0
l=len(a)
print(l)

for i in range(0,len(a)-5,1):
    if (a[i]==a[i+1] and a[i+1]==a[i+2] and a[i+2]==a[i+3] and a[i+3]==a[i+4] and a[i+4]==a[i+5] ):
        count+=1
print("loop exor")      
print(count)


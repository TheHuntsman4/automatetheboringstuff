import random,time
for q in range(1,11):
    a=random.randint(0,9)
    b=random.randint(0,9)
    ans=a*b
    flag=0
    time1=time.time()
    print("%s: %sx%s = "%(q,a,b))
    for i in range(3):
        user=int(input())
        if user==ans:
            flag=1
            if flag==1:
                time2=time.time()
                time3=time2-time1
                break
        else:   
            print("incorrect answer")
    if flag==1:
        if time3<=8:
            print("correct")
        else:
            print("times up ")

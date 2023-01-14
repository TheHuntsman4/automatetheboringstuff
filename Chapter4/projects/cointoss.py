import random
numberOfStreaks = 0
for experimentNumber in range(1,10001):
    # Code that creates a list of 100 'heads' or 'tails' values.
    ls=[]
    for i in range(100):
        toss=random.randint(0,1)
        ls.append(toss)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak=0
    for j in ls:
        if j==0:
            streak+=1
            if streak==6:
                numberOfStreaks+=1
                break
        else:
            
            streak=0
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

import sys
def collatz(number):
        if(number%2==0):
            number=number//2
        else:
            number=3*number+1
        print(number)
        while(number!=1):
            collatz(number)
        sys.exit()

n=int(input("ENTER A NUMBER "))
collatz(n)

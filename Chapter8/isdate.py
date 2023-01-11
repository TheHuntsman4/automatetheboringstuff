import re
date=[2]
month=[2]
year=[4]
isdate=re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
ob=isdate.search('04/06/2004')
if ob:
    date=int(ob.group(1))
    month=int(ob.group(2))
    year=int(ob.group(3))
    print(date,month,year)
else:
    print("invalid date")
def check_year(year):
    if(year>=1000 and year<=2999):
        if(year%4==0 or year%400):
            return 2
        else:
            return 1 
    else:
        return 0
def check_month(month,year):
    if(month>=1 and month=<12):
        return 1
    else:
        return 0
def check_date(day):
    if(day>=1 and day<=31):
        return 1
    else:
        return 0

def validation(day,month,year):
     if(check_year(year)==1 or check_year(year)==2):
         if(check_month(month)==1):
             if(
         

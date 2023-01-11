import re
date=[2]
month=[2]
year=[4]
isdate=re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
ob=isdate.search('04/06/2004')
if ob:
    date=ob.group(1)
    month=ob.group(2)
    year=ob.group(3)
    print(date,month,year)
else:
    print("invalid date")

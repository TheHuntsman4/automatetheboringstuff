import re
date=[2]
month=[2]
year=[4]
date_30=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
date_31=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
month_30=['04','06','09','11']
month_31=['01','03','05','07','08','10','12']
isdate=re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
ob=isdate.search('31/06/2004')
if ob:
    day=ob.group(1)
    month=ob.group(2)
    year=int(ob.group(3))
    
    if((year>1000 and year<2999)):
        if(year%4==0 or year%400==0):
            if(month=='02'):
                if(day>29):
                    print("invalid date")
                else:
                    print("valid date")
        
        if month in month_30:
            if day in date_30:
                print("valid date")
            else:
                print("invalid date")
        elif month in month_31:
            if day in date_31:
                print("valid date")
            else:
                print("invalid date")
        else:
            print("invalid date")

                
            


else:
    print("invalid date")

import re
test='abc'
def password_check(test):
    password=re.compile(r'\w{8,}[A-Z]\d{1,}')
    ob=password.search(test)
    if ob:
        print(ob.group())
    else:
        print("password not strong")
i=input("enter your password")
password_check(i)

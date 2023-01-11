import re
test='abcdefghQQ1234565'
password=re.compile(r'\w{8,}[A-Z]\d{1,}')
digit=re.compile(r'\d{1,}')
caps=re.compile(r'[A-Z]')
ob=password.search(test)
ob1=digit.search(test)
ob2=caps.search(test)
print(ob.group(0))
if ob:
    print(ob1.group())
if ob and ob2 and ob1 :
    print("yes")

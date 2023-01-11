import re
s=1

test=' new line '






strip_regex=re.compile(r'^\S')
ob=strip_regex.findall(test)
print(''.join(ob))

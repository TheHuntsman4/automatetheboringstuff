import re
test=" newline "
strchr=" "
strip_regex=re.compile(r'^{'+str(strchr)+'}')
ob=strip_regex.sub("",test)
print(ob)

import pprint
message='the hungry fox jumped over the lazy sheep'

count={}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1
pprint.pprint(count)

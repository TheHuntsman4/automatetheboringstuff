test1={'1a':'wking', '6c': 'wqueen', '2g': 'bbishop', '2h': 'bknight', '3e': 'bking','1h':'bqueen','4a':'bpawn','4b':'bpawn','4c':'bpawn','4d':'bpawn','4e':'bpawn','4f':'bpawn','4g':'bpawn','4h':'bpawn','5a':'wpawn','5b':'wpawn','5c':'wpawn','5d':'wpawn','5e':'wpawn','5f':'wpawn','5g':'wpawn','5h':'wpawn'}
test2={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
def isValidChessBoard(dic):
    flag=0
    loc=[]
    for i in range(1,9):
        for j in ['a','b','c','d','e','f','g','h']:
            ele=str(i)+str(j)
            loc.append(ele)
    on_board=0
    pieces=dic.values()
    count={}
    for i in pieces:
        count.setdefault(i,0)
        count[i]=count[i]+1
        on_board+=1
    if on_board!=32:
        flag=1
    if (count.keys()=='bking' or count.keys()=='wking'):
        if count.value()!=1:
            flag=1
    elif(count.keys()=='bpawn' or count.keys()=='wpawn'):
        if count.value!=8:
            flag=1

    for i in dic.keys():
        if i not in loc:
            flag=1
    if 2 in list(count.values()):
        flag=1





    if flag==1:
        return False
    else:
        return True
print("this is test 1 ",isValidChessBoard(test1))
print("this is test 2 ",isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))

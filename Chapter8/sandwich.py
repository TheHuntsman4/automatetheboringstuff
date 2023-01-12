import pyinputplus as pyip
cost=0
bread_dic={"wheat":30,"white":40,"sourdough":50}
protein_dic={"chicken":30,"turkey":40,"ham":50,"tofu":60}
cheese_dic={"cheddar":30,"swiss":30,"mozzarella":30}
extra_dic={"mayo":10,"mustard":10,"lettuce":15,"tomato":15}

    
bread=pyip.inputMenu(['wheat','white','sourdough'],prompt="enter type of bread:\n")
cost+=bread_dic[bread]
protein=pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt="enter type of protein:\n")
cost+=protein_dic[protein]
choice=pyip.inputYesNo(prompt="do u want cheese:\n")
if choice=='Yes' or choice=='yes':
        cheese=pyip.inputMenu(['cheddar','swiss','mozzarella'])
        cost+=cheese_dic[cheese]

else: 
    cheese="no cheese"
choice=pyip.inputYesNo(prompt="do u wish to hav extras\n")
if choice=="Yes" or choice=='yes':
    extra=pyip.inputMenu(["mayo","mustard","lettuce","tomato"])
    cost+=extra_dic[extra]
else:
    extra="no extras"
n=pyip.inputInt(prompt="enter the number of sandwiches:\n",min=1)
    
print("Your total is ",n*cost)

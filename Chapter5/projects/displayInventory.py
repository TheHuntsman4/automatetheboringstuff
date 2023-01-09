i={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inv):
    number=list(inv.values())
    item=list(inv.keys())
    print("INVENTORY:")
    for i in range(len(item)):
        print(number[i],item[i])
        
displayInventory(i)    

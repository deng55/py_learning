print('Simple Assignment')
shoplist=['apple', 'mango', 'carrot', 'banana']

myList = shoplist

del shoplist[0]

print('shopList is',shoplist)
print('myList is', myList)

myList = shoplist[:]

del myList[0]

print('shopList is',shoplist)
print('myList is', myList)
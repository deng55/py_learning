shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('these items are:', end=' ')
# 使用end=' ' 来结束，可以替换\n 换行操作
for i in shoplist:
    print(i,end=' ')

print('\n I also want to buy rice.')
shoplist.append('rice')
print('my shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
oldItem = shoplist[0]
del(shoplist[0])
print('I brought the ', oldItem)
print('My shopping list now is', shoplist)

help(list)
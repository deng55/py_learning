motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0]='ducati'
print(motocycles)

# 添加元素
motocycles.append('ducati')
print(motocycles)

# 插入元素
motocycles.insert(0, 'hello')
print(motocycles)

# 刪除元素 知道要刪除的元素的位置 用 del
del motocycles[0]
print(motocycles)

# 刪除末尾的元素 用pop()  也可以使用pop(index)刪除指定位置的元素
moto = motocycles.pop()
print(motocycles)
print(moto)

# 直接刪除值 使用remove()
# motocycles.remove('hello')
motocycles.remove('ducati')
print(motocycles)

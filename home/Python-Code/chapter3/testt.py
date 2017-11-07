guests = ['jack', 'tom', 'jerry']
print(guests)
print('I will invite'+str(guests) + 'to my party')

guests[0]='lily'
print(guests)
guests.insert(0, 'henry')
print(guests)
guests.insert(2, 'good')
print(guests)
guests.append('dog')
print(guests)

# 排序
guests.sort()
print(guests)
# 倒序排序
guests.sort(reverse=True)
print(guests)

# 臨時排序
print(sorted(guests,reverse=True))
print(guests)
print(guests.reverse())# 倒着打印
print(len(guests))

for value in range(1,5):
    print(value)


nums = list(range(1,6))
print(nums)

num2 = list(range(1,20,3))#步进
print(num2)
min(nums)
max(nums)
a=sum(nums)
print(a)

#列表解析 生成列表
squares = [value**2 for value in range(1,11)]
print(squares)

qube = [qube**3 for qube in range(1,11)]
print(qube)

no = range(1,1000)
for n in no:
    print(n)

    # 使用切片来复制操作
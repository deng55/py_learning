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
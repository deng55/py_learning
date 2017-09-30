def total(a=5, *numbers, **phonebook):
    print('a',a)


    # 遍历元组中的所有项目 *param  元组
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历所有字典中的项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10,1,2,3, jack=1122, john = 2233, inge=5566))

def some_function() :
    pass

print(some_function())


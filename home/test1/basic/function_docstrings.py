def print_max(x, y):
    '''Prints the maximum of two numbers, 打印两个数值中的最大值
    the two values must be integer.'''

    x = int(x)
    y = int(y)

    if x>y:
        print(x, "is maximum")
    else:
        print(y, 'is maximum')

print_max(3, 5)
# print(print_max.__doc__)

help(print_max)
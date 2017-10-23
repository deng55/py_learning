L = [x * x for x in range(10)]
print(L)  # 列表生成器

# 创建生成器
g = (x * x for x in range(10))
print(g)
for x in g:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        return 'done'


s = fib(6)
while True:
    try:
        y = next(s)
        print("g:", y)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


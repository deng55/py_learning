def triangles(max):
    n = 1
    g = [1]
    while len(g)<max+1:
        yield g
        for i in range(1,len(g)):
            print(i)

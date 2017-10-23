def magician(magicians):
    for magic in magicians:
        print(magic)


ma = ['hello1', 'hello2', 'hello3']

magician(ma)

great_mac = []
def make_great(mac):
    while mac:
        m = mac.pop()
        great_mac.append('the great '+m)
    # for index, m in enumerate(mac):
    #     mac[index]="the great"+m


make_great(ma[:])

magician(great_mac)
magician(ma)

def make_pizza(size,*toppings):
    '''打印顾客点的所有配料'''

    print('making a '+str(size)+ ' inch pizza with '
                                 'follow toppings:')
    for topping in toppings:
        print('-'+topping)
    # print(toppings)

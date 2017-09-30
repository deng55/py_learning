number = 23
running = True

while running:
    guess = int(input("enter an integer:"))

    if guess == number:
        print("good luck")
        running = False
    elif guess < number:
        print("this is lower than that")
    else:
        print("this is higher than that")
else:
    print('the loop is over')

    print('done')
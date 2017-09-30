try:
    text = input("enter something-->")
except EOFError:
    print("why did you do a efo error on me")
except KeyboardInterrupt:
    print("keyboard exception")
else:
    print('you entered {}'.format(text))


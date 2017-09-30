class ShortInputException(Exception):
    def __init__(self,length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('enter something-->')
    if len(text)<3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('why did you do an eof error on me')
except ShortInputException as ex:
    print(('ShortInputException : the input was ' +
           '{0} long, excepted at least {1}').format(
        ex.length, ex.atleast
    ))
else:
    print("no exception raised")

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("enter text:")
if is_palindrome(something):
    print("yes, it's a palindrome")
else:
    print("it's not a palindrome")
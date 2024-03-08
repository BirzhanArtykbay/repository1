def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_string = input()
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
'''Check whether the given string is palindrome or not  a) with slicing b) without using slicing'''
s= input("Enter a string:")
if s == s[: :-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")
'''part2'''
t=input("Enter a string:")
trev=''
for char in t:
    trev=char+trev
if t == trev:
        print("String is palindrome")
else:
    print("String is not palindrome")

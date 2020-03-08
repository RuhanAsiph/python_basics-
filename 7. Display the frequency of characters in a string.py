s = input("Enter a string:")
dict={char:s.count(char) for char in s}
print(dict)

s = input("Enter a Sentence:")
blanks = s.count(' ')
vowels=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
consonants = len(s)-blanks - vowels
print("Total number of:")
print("Vowels=", vowels)
print("Consonants=", consonants)
print("Blank Spaces=", blanks)

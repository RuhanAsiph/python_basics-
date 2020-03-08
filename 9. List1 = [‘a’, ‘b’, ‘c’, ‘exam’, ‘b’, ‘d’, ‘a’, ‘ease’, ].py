'''9. List1 = [‘a’, ‘b’, ‘c’, ‘exam’, ‘b’, ‘d’, ‘a’, ‘ease’, ].
a. Write a program by considering the above list to display single occurrence
of the elements of the list, to display only the repetitive elements of the
list, to display the elements whose length of the element is 1'''
List1 = ['a', 'b', 'c', 'exam', 'b', 'd', 'a', 'ease']
unique = []
not_unique = []
single = []
for ele in List1:
    if List1.count(ele) ==1:
        unique.append(ele)
    else:
        not_unique.append(ele)
    if len(ele)==1:
        single.append(ele)
print("Elements with single occurence:", unique)
print("Elements with Multiple occurence:" ,set(not_unique))
print("Elements whose length is 1:", single)

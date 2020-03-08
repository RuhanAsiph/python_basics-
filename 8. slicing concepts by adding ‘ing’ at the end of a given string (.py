s = input("Enter a string:")
if len(s)>=3:
    if(s[-3:]=="ing"):
        s=s.replace(s[-3:],'ly')
    else:
        s=s+'ing'
print(s)
        

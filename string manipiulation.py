line=input("enter a line:")
lowercount=uppercount=0
digitcount=alphacount=0
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphacount +=1
print("number pf uppercase letter:",uppercount)
print("number of lowercase letter:",lowercount)
print("number of alphabets:",alphacount)
print("number of digit :",digitcount)

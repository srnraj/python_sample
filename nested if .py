student = input('enter a name:')
mark = int(input('enter a number:'))
if mark <0 or mark >100:
    print('invalid marks')
else:
    if mark > 75:
        print(student, 'scored a above avarage mark',mark)
    else:
        if mark <= 75 and mark >=35:
            print(student,' scored a avarage mark',mark)  
        else:  
            print(student,' scored a poor mark',mark)  



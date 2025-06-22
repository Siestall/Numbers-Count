num = list(input("Enter integer: "))
try:
    num2 = [int(x) for x in num]
    count = 0
    for i in range(10):
        if num2.count(i) == 0:
            continue
        else:    
            print(f'{i} --> {num2.count(i)}')
            count+=1
    if count != 10:
        print('There are no other numbers')
except:
    print('Enter integer')

num = list(input("Введите число: "))
try:
    num2 = [int(x) for x in num]
    c = 0
    for i in range(10):
        if num2.count(i) == 0:
            continue
        else:    
            print(f'{i} --> {num2.count(i)}')
            c+=1
    if c != 10:
        print('Остальных 0')
except:
    print('Enter integer')
    

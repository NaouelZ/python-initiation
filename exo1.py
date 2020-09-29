displayed = []

def ThreeDigit () :
    for i in range(999):
        l = list(str(f'{i:03}'))
        number = f'{i:03}'
        if number not in displayed:
            displayed.append(number)
            if l[0] != l[1] and l[1] != l[2] and l[2] != l[0] :
                print(number)        
        
ThreeDigit()

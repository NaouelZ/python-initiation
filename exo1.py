def ThreeDigit () :
    for i in range(999):
        l = list(str(f'{i:03}'))
        if l[0] != l[1] and l[1] != l[2] and l[1] != l[0] :
            print(f'{i:03}')
        
ThreeDigit()
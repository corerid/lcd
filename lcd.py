def lcd(number):
    out = []
    res = ""
    number = str(number)
    num_len = len(number)
    # print (num_len)
    for i in range(num_len):
        if number[i] == '1':
            out.append([[' ',' ',' '],
                        [' ','|',' '],
                        [' ','|',' ']])
        elif number[i] == '2':
            out.append([[' ','_',' '],
                        [' ','_','|'],
                        ['|','_',' ']])
        elif number[i] == '3':
            out.append([[' ','_',' '],
                        [' ','_','|'],
                        [' ','_','|']])
        elif number[i] == '4':
            out.append([[' ',' ',' '],
                        ['|','_','|'],
                        [' ',' ','|']])
        elif number[i] == '5':
            out.append([[' ','_',' '],
                        ['|','_',' '],
                        [' ','_','|']])

    for j in range(3):
        for i in range(num_len):
            for k in range(3):
                res += out[i][j][k]
        res += '\n'
    return res
    
res = lcd(12345)
print (res)


    

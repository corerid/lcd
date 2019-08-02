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

    k = 0
    for j in range(3):
        for i in range(num_len):
            for k in range(3):
                # print (i,j,k)
                res += out[i][j][k]
        res += '\n'

    # print res

    return res
    
res = lcd(123)
print (res)


    

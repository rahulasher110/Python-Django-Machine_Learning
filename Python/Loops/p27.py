i = 1
while i <= 5:
    print('begin :- ',i)

    for j in range(10,12):
        print('inner :- ',i,j)
    print('end :- ',j)
    i += 1

print('program end')
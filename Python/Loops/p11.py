print('begin')

for i in [10,20,'abc',12.3,'hello',True]:
    print('begin value :- ',i)

    if i == 'abc':
        break
        print('loop end with an index :-  ',i)

    print('end value :- ',i)
print()
print('end')
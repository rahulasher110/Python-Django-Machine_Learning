print('begin')

for i in [10,20,'abc',12.3,'hello',True]:
    print('begin value :- ',i)

    if i == 'abc':
        print('loop break with an index :- ',i)
        break

    print('end value :- ',i)
print()
print('end')
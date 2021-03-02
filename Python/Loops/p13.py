print('begin')

for i in [10,20,'abc','hello',True,12.33]:

    print('loop begin with an index :- ',i)

    if i == 'hello':
        continue

    print('loop end with an index :- ',i)

print()
print('end')
for i in range(5):
    print('i am in the outer begin :- ',i)

    for j in range(10,13):
        print('i am in the inner loop begin :- ',i,j)

        if j == 11:
            continue

        print('i am in the inner loop end :- ',i,j)

    print('i am in the outer end :- ',i)

print()
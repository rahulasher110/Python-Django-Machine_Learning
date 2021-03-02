def f1():
    print(1)
    def f11():
        print(2)
        print(3)
        print(4)
    print(5)

    f11()
    print('----------')

    f11()
    print('---------------')


f1()
print('-------------------')

f1()
print('--------------------')


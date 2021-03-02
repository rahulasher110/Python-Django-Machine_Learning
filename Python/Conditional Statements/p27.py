def test(arg1):
    def c1():
        print(' i am form c1')
        print(' i am form c1')

    def c2():
        print('i am from c2')
        print('i am from c2')

    def c3():
        print('i am from c3')
        print('i am from c3')

    d1 = {

        # dictionary
        1 : c1,
        2 : c2,
        3 : c3,
    }

    d1.get(arg1)()
test(2)

test(1)
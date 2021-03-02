x = 100

def test():
    x = 10
    print(x)

def test1():
    x = 20
    print(x)
    
def test2():
    global x
    print(x)
    x = 430
    print(x)

test()
test1()
test2()

print(x)
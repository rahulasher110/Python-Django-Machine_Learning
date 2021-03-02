x = {'k1' : 'hello', 'k2' : 123, 4.5 : True, 'abc' : 3.4 , False : 'py'}

print(x, type(x))

for i in x:
    print(i)

print('------------------')

for i in x.values():
    print(i)
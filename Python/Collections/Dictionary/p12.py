x = {'k1' : 'hello', 'k2' : 123, 4.5 : True, 'abc' : 3.4 , False : 'py'}

print(x, type(x))

x.pop('k1')
print(x)

x.pop('abc')
print(x)
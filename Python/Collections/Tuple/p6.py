x = (1,2,3,4,5,6,6,6545)

print(x, type(x))

y = list(x)
y[0] = 'rahul singj'
print(y, type(y))

x = tuple(y)
print(x, type(x))

x = [12,343434,'abc']
y = [32,'abc',True]

print(x)
print(y)

print('----------------------')

y.extend(x)
z = list(x)

print(x)
print(y)
print(z)
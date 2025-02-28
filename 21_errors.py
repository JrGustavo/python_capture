#print(0/0)
#print(result)
print('Hola')

suma = lambda x, y: x + y
assert suma(1, 2) == 3

print('Hola 2')

age = 10
if age < 2:
    raise Exception('Age must be greater than 2')
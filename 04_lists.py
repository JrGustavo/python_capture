# number = []
# for element in range(1, 11):
#     number.append(element)
#
# print(number)
#
# numbers_v2 = [element for element in range(1, 11)]

numbers = []
for i in range(1, 11):
    if i % 2 == 0:
     numbers.append(i * i)

print(numbers)
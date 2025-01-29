def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1

result = increment(10)
print(11)

result = increment_v2(10)
print(11)

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

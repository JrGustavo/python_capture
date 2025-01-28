dict = {}
for i in range(1, 11):
        dict[i] = i * i

print(dict)

import random
countries = ['col', 'Australia', 'Germany', 'France']
population = {}
for country in countries:
    population[country] = random.randint(1000000, 10000000)
print(population)


population_v2 = {country: random.randint(1000000, 10000000) for country in countries}
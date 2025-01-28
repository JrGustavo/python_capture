set_countries = {'USA', 'Canada', 'UK', 'Australia', 'Germany', 'France'}

size = len(set_countries)
print(size)

print('USA' in set_countries)
print('India' in set_countries)


#add
set_countries.add('India')
print(set_countries)
set_countries.add('USA')
print(set_countries)

#update
set_countries.update(['China', 'Japan', 'Russia'])
print(set_countries)

#remove
set_countries.remove('China')
print(set_countries)

set_countries.remove('China')
set_countries.discard('China')
print(set_countries)
set_countries.discard('China')
print(set_countries)

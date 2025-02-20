
items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

def add_taxes(item):
    new_item = item.copy()
    item['price'] = item['price'] * 1.16
    return new_item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)
print('Old list')
print(items)
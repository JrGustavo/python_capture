items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

new_items = list(map( lambda x: x|{'tax': x['price']*0.19} ,items))

print(new_items)
print(items)
price = 100   #global

def increment():
    price = 200
    result = price + 10
    print(price)
    return result


print(price)
price_2 = increment()
print(price_2)


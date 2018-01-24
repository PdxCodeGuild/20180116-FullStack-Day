


product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}

print(product_to_price)


product_to_price['banana'] = 1.25


print(product_to_price)


for key in product_to_price:
    print(f'{key} {product_to_price[key]}')


for key, value in product_to_price.items():
    print(f'{key} {value}')



keys = list(product_to_price.keys())
keys.sort()

print(keys)

for key in keys:
    print(f'{key} {product_to_price[key]}')


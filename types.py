

def format_price(price):
    price = float(input('Введите price: '))
    price = str(price)
    return f'Цена: {price} руб.'
    
p = format_price(68.25)
print(p)

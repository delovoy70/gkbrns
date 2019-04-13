import json
import datetime

def write_order_to_json(item, quantity, price, buyer, date):

    dict_for_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'w') as f_n:
        json.dump(dict_for_json, f_n, indent=4)


write_order_to_json('bread', 'best', 50.9, 'private person', datetime.datetime(2019,1,15,9,15,59).isoformat())

import json

def write_order_to_json(item, quantity, price, buyer, date):
    filename = 'orders.json'
    data = {}
    with open(filename, encoding="utf-8") as fl:
        data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(filename, "w", encoding="utf-8") as fl:
            json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)



if __name__ == '__main__':
    write_order_to_json('Телефон teXet TM-D328', '1', '1690', 'Иванов И.И.', '28.02.2022')
    write_order_to_json('Ноутбук HONOR MagicBook X', '1', '59990', 'Петров П.П.', '28.02.2022')
    write_order_to_json('Холодильник Hyundai CO1003', '1', '11995', 'Сидоров С.С.', '28.02.2022')

with open('orders.json', encoding='utf-8') as f_n:
    print(f_n.read())
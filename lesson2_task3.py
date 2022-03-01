import yaml

data = {
    'items': ['фунты стерлингов', 'доллары', 'юань', 'евро'],
    'items_quantity': 4,
    'items_price': {
        'pound sterling': '200£',
        'dollars': '50$',
        'yuan': '475¥',
        'euro': '100€'
    }
}

with open('file.yaml', 'w',encoding='utf-8') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml',encoding='utf-8') as f_n:
    print(f_n.read())
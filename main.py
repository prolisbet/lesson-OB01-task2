# *Дополнительное задание:
# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также
# существуют общие характеристики, такие как адрес, название и
# ассортимент товаров. Ваша задача — создать класс `Store`,
# который можно будет использовать для создания различных магазинов.
#
# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена.
#           Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и
# добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы:
# добавь товар, обнови цену, убери товар и запрашивай цену.


class Store():
    def __init__(self, name, address, items={}):
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, item, price):
        self.items[item] = price
        print(f'Добавлен новый товар - {item}.')
        print(f'Цена товара - {price}. \n')

    def delete_item(self, item):
        if item in self.items:
            print(f'Товар {item} удален. \n')
            self.items.pop(item, None)
        else:
            print('Товар отсутствует в ассортименте. \n')

    def get_price(self, item):
        if item in self.items:
            price = self.items[item]
            print(f'Цена товара {item} - {price}. \n')
        else:
            print(None, '\n')

    def renew_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
            print(f'Новая цена товара {item} - {new_price}. \n')
        else:
            print('Товар отсутствует в ассортименте. \n')

    def info(self):
        print(f'Название магазина - {self.name}.')
        print(f'Адрес магазина - {self.address}.')
        print('Ассортимент магазина:')
        for index, (key, value) in enumerate(self.items.items(), start=1):
            print(f'{index}. {key} - {value}.')
        print()


store1 = Store('Пятерочка', 'Жулебинский б., д.25', {'яблоки':100, 'груши':130})
store2 = Store('Продукты', 'ул. Летчика Ларюшина, д.4', {'чипсы':110, 'Corona':180})
store3 = Store('Дикси', 'Комсомольский пр., д.28', {'картошка':50, 'перец':330})

store1.info()
store2.info()
store3.info()

store1.add_item('мандарины', 120)
store1.renew_price('яблоки', 110)
store1.renew_price('картошка', 60)
store1.delete_item('груши')
store1.delete_item('картошка')
store1.get_price('мандарины')
store1.get_price('перец')
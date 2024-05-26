class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item '{item_name}' not found.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Item '{item_name}' not found.")

    def __repr__(self):
        return f"Store(name='{self.name}', address='{self.address}', items={self.items})"

# Пример использования
store = Store("Магазин Продукты", "ул. Ленина, д. 1")
store.add_item("яблоки", 0.5)
store.add_item("бананы", 0.75)

print("Ассортимент магазина:")
print(store)

store.update_item_price("яблоки", 0.6)
store.remove_item("бананы")

print("Ассортимент магазина после обновлений:")
print(store)
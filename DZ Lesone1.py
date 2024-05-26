class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_completed(self):
        self.status = True

    def __repr__(self):
        return f"Task(description='{self.description}', deadline='{self.deadline}', status={'Completed' if self.status else 'Not Completed'})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Invalid task index.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.status]

task_manager = TaskManager()
task_manager.add_task("Сделать домашнее задание", "2024-05-30")
task_manager.add_task("Сходить в магазин", "2024-05-26")

print("Текущие задачи:")
for task in task_manager.get_current_tasks():
    print(task)

task_manager.mark_task_as_completed(0)

print("Текущие задачи после выполнения одной задачи:")
for task in task_manager.get_current_tasks():
    print(task)


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


store1 = Store("Магазин Продукты", "ул. Ленина, д. 1")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2 = Store("Магазин Электроника", "ул. Карла Маркса, д. 5")
store2.add_item("laptop", 500)
store2.add_item("smartphone", 300)

store3 = Store("Магазин Одежда", "ул. Пушкина, д. 10")
store3.add_item("jeans", 40)
store3.add_item("t-shirt", 20)


print("Ассортимент магазина до обновлений:")
print(store1)

store1.add_item("oranges", 0.6)
store1.update_item_price("apples", 0.6)
store1.remove_item("bananas",)

print("Ассортимент магазина после обновлений:")
print(store1)
print("Цена на яблоки:", store1.get_item_price("apples"))
print("Цена на бананы:", store1.get_item_price("bananas"))



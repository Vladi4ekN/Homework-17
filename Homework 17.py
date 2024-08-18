class House:
    houses_history = []  # Атрибут класса для хранения названий зданий

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors  # Возвращает количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # Возвращает строку с информацией о доме

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors  # Сравнение по количеству этажей

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors  # Меньше

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors  # Меньше или равно

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors  # Больше

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors  # Больше или равно

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors  # Не равно

    def add(self, value):
        self.number_of_floors += value  # Увеличиваем количество этажей
        return self  # Возвращаем сам объект

    def radd(self, value):
        return self.add(value)  # Работает так же, как и add

    def iadd(self, value):
        return self.add(value)  # Работает так же, как и add

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

# Примеры использования класса House
house1 = House('ЖК Эльбрус', 30)
house2 = House('ЖК Снегири', 25)
house3 = House('ЖК Лесной', 15)

# Проверка работы метода del
del house1

# Проверка значения атрибута houses_history
print(House.houses_history)
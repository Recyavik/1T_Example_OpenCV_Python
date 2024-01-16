class Person:
    def __init__(self, name='Неизвестно', age=None):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет, меня зовут {self.name}"

    def celebrate_birthday(self):
        return f"Мне {self.age} лет"

person = Person()
person.name = "Михаил"
person.age = 16
print(person.greet())
print(person.celebrate_birthday())
class Person:
    def __init__(self, name: str ='Не задано', age: int =0):
        self.name = name
        self.age = age

    def input_data(self):
        self.name = input('Введите ваше имя: ')
        self.age = int(input('Введите ваш возраст: '))
        return self.name, self.age

    def introduce(self, name, age):
        print(f'Привет, меня зовут {name}, мне {age} лет.')

men = Person()
men.input_data()
men.introduce(men.name, men.age)


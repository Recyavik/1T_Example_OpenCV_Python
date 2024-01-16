class Cat:
    def __init__(self, name, breed, age, color):
       self.name = name
       self.bread = breed
       self.age = age
       self.color = color

    def print_info(self):
        print(f'Имя: {self.name}, порода: {self.bread}, возраст: {self.age}, окрас: {self.color}.')


cat1 = Cat('Барсик', 'дворовый', 3, 'рыжий')
cat1.print_info()
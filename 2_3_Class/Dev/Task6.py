class Human:
    name = None
    def __init__(self):
        self.name = input('Как вас зовут: ')

    def Eat(self):
        print(f'{self.name} is eating.')

    def Sleep(self):
        print(f'{self.name} is sleeping.')

    def Work(self):
        print(f'{self.name} is working.')

h = Human()
# h.name = 'Михаил'
h.Eat()
h.Sleep()
h.Work()

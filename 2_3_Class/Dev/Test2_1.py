class House:
    is_roof_created = False
    is_walls_created = False

    def create_walls(self):
        print('Построили стены')
        self.is_walls_created = True

    def create_roof(self):
        if self.is_walls_created == True:
            print('Построили крышу')
            self.is_roof_created = True
        else:
            print('Нельзя построить крышу раньше стен')

    def create_house(self):
        if self.is_walls_created == True and  self.is_roof_created == True:
            print('Построили дом')
        elif self.is_roof_created == False and self.is_walls_created == True:
             print('Нельзя построить дом раньше крыши')
        elif self.is_roof_created == True and self.is_walls_created == False:
             print('Нельзя построить дом раньше стен')
        else:
            print('Нельзя построить дом')


house1 = House()
house1.create_house()
house1.create_walls()
house1.create_house()
house1.create_roof()
house1.create_house()

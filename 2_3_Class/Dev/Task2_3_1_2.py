def get_user_data():
    name = input('Введите ФИО: ')
    email = input('Введите почту: ')
    number = input('Введите номер телефона: ')
    return name, email, number

name, email, number = get_user_data()
print('ФИО:',name)
print('Почта:',email)
print('Номер телефона:',number)

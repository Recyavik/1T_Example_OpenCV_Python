# Создайте файл с именем "names.txt". Запишите в него введенную с клавиатуры строку 10 тысяч раз через пробел.
# Для создания используйте конструкцию with open. Произведите операцию записи методом write.

line = input('Введите строку:') + ' '

with open('names.txt', 'w') as file:
    file.write(line*10000)

    
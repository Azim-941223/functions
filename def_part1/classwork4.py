def fileCreat(file_name):
    with open(file_name,'w') as file:
        pass
    return 'Файл создан'

file_Name = input('Введите название файла: ')
file = fileCreat(file_Name)
print(file)
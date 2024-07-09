# Импорт необходимых библиотек
import os  # Работа с операционной системой, включая управление файлами и папками

# Работа с файлами

# Открытие файла для чтения
# Режимы открытия файла:
# 'r' - чтение (по умолчанию)
# 'w' - запись (создает новый файл или перезаписывает существующий)
# 'a' - добавление (открывает файл для добавления данных в конец)
# '+' - чтение и запись

file_path = 'example.txt'  # Путь к файлу

# Чтение из файла
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()  # Чтение всего содержимого файла
    print(content)  # Вывод содержимого файла

# Запись в файл
with open(file_path, 'w', encoding='utf-8') as file:
    file.write('Это пример записи в файл.\n')  # Запись строки в файл
    file.write('Еще одна строка.\n')  # Запись еще одной строки

# Добавление в файл
with open(file_path, 'a', encoding='utf-8') as file:
    file.write('Добавляем строку в конец файла.\n')  # Добавление строки в конец файла

# Чтение файла построчно
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # Чтение и вывод каждой строки файла

# Открытие файла для чтения и записи
with open('example.txt', 'r+', encoding='utf-8') as file:
    content = file.read()  # Чтение всего содержимого файла
    file.write('Добавляем строку после чтения.\n')  # Запись в файл


# Управление файлами и директориями

# Проверка существования файла или директории
file_exists = os.path.exists(file_path)
print(f'Файл существует: {file_exists}')

# Создание новой директории
new_dir = 'new_directory'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)  # Создание новой директории

# Переименование файла или директории
new_file_path = 'new_example.txt'
os.rename(file_path, new_file_path)  # Переименование файла

# Удаление файла
if os.path.exists(new_file_path):
    os.remove(new_file_path)  # Удаление файла

# Удаление директории
if os.path.exists(new_dir):
    os.rmdir(new_dir)  # Удаление пустой директории

# Список файлов в директории
current_directory = '.'
files = os.listdir(current_directory)
print(f'Файлы в текущей директории: {files}')

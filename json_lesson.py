# Импорт библиотеки для работы с JSON
import json

# Пример данных для записи в файл JSON
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}

# Запись данных в файл JSON
file_path = 'data.json'
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(f'Данные успешно записаны в файл: {file_path}')

# Чтение данных из файла JSON
with open(file_path, 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

# Вывод загруженных данных
print('\n Загруженные данные из файла:')
print(f"Имя: {loaded_data['name']}")
print(f"Возраст: {loaded_data['age']}")
print(f"Город: {loaded_data['city']}")
print("Навыки:")
for skill in loaded_data['skills']:
    print(f"- {skill}")

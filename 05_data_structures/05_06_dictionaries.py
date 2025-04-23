"""Структуры данных — словари."""

person1 = {
    'name': 'Petr',
    'age': 20,
    'gender': 'male',
    'name': 'Ivan',
    # Ключи словаря не могут дублироваться!
    # Дубликат ключа, заменяет старый
    'roles': {'dev': "developer", 'test': 'Tester'}
    # Вложенный словарь

}

person2 = {
    'age': 20,
    'gender': 'male',
    'name': 'Ivan',
    'roles': {'dev': "developer", 'test': 'Tester'}
}

print("Словарь person1:", person1)
print("Словарь person2:", person2)
print("Обращение по ключу person1['age']:", person1['age'])
# Если ключ не существует, ошибка KeyError

print("Сравнение словарей, словари равны?:", person1 == person2)

print("Обращение к вложенному словарю:", person1['roles']['test'])

print('\nМетод get:')
print("Обращение с помощью get", person1.get('name'))
print("Обращение с помощью get, к не существующему ключу, вернёт None:",
      person1.get('test'))
# Если ключ не существует, get вернёт None

print('\nЗначение по умолчанию:')
print(person1.get('name', 'No name'))
print(person1.get('gender', 'male'))

print('\nДоступ к ключам и значениям:')
print("keys возвращает ключи словаря:", person1.keys())
print("values возвращает значения словаря:", person1.values())
print("items возвращет кортежи (ключ и значение):", person1.items())
# Возвращаемые значения можно индексировать и перебирать, но нельзя изменять!

print('\nПростой перебор выполняется только по ключам:')
for x in person1:
    print(f'Ключ: {x}')

print('\nПеребор элементов словаря:')
for key, value in person1.items():
    # возвращает пару ключ: значение и распаковывает их
    print(f'Ключ {key} соответствует значению {value}')

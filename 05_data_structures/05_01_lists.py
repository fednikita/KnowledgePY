"""Структуры данных — списки."""

print("Основы списков")
empty = []  # Пустой список
fruits = ['apple', 'banana', 'peach', 'strawberry']  # Элементы одного типа
different = ['text', 23, 3.14, 9.20, False]  # Элементы разных типов
print(fruits)
print("Обращения по индексу:")
print(fruits[2])  # Каждый элемент доступен по индексу
print(fruits[-3])  # Все правила аналогичны работе со строками
print(fruits[0:3])
print("Перезаписанный список:")
# Списки изменяемы, можно перезаписать:
fruits = [
    'apple',
    'peach',
    'banana',
    'peach',
    'strawberry',
    'peach',
    'apple'
]
# Списки могут содержать дубликаты
print(fruits)

print("\nВложенные списки")

nested_list = [
    [0, 1, 2],
    ['apple', 'banana', 'cherry'],
]

print(nested_list[1][2])

print("\nМногоуровневые вложенные списки")
list_of_list = [
        [0, 1, 2],  # Первый подсписок
        [           # Второй подсписок
            'apple',
            'banana',
            ['cherry', 'damson'],  # Вложенный список
        ],
    ]

print(list_of_list[1][2][1])

print("\nЗамена одного элемента списка")
print('До замены:', fruits)
fruits[1] = 'grapes'  # Заменим второй элемент списка
print('После замены:', fruits)

print("\nЗамена нескольких элементов списка")
fruits[1:4] = ['BANANA', 'PEACH', 'STRAWBERRY', 'WATERMELON']
# Дополнительный элемент подставится автоматически
print('После замены:', fruits)

print("\nОбъединение списков")
print('Дополнительный список:', ['strawberry', 'mango'])
fruits = fruits + ['strawberry', 'mango']
# + создаёт новый список с обновлёнными элементами
print('После объединения:', fruits)

print("\nВстроенные методы списков")
print("Удаление всех элементов списка clear()")
fruits.clear()
print('После удаления:', fruits)

print("\nДобавление элементов extend()")
# extend обновляет старый список, не создавая новый
fruits.extend(['apple', 'banana', 'grapes', 'peach'])
print('После добавления:', fruits)

print("\nДобавление одного элемента в конец списка append()")
fruits.append('strawberry')
print('После добавления:', fruits)

print("\nВставка элемента по индексу insert()")
fruits.insert(2, 'cherry')
print('После добавления:', fruits)

print("\nУдаление элемента по индексу del()")
del fruits[1]
print('После удаления:', fruits)

print("\nУдаление элемента по значению remove()")
fruits.remove('peach')
print('После удаления:', fruits)

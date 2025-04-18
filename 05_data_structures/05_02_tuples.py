"""Структуры данных — кортежи."""
# Кортежы не изменяемы
# Кортеж определяется с помощью ()
empty_tuple = ()
# Если кортеж не пустой, скобки не обязательны, но это ухудшает читаемость
fruits_tuple = ('apple', 'banana', 'peach', 'strawberry', 'apple')
mixed_tuple = ('Text', 12, 3.45, True)

hello_str = ('Hello wolrd!')
hello_tuple = ('Hello wolrd!',)

print("При определении кортежа , обязательна:")
print('tuple_str содержит:', type(hello_str))
print('tuple_tuple содержит:', type(hello_tuple))


original_tuple = (1, 2, 3)
shuffled_tuple = (3, 2, 1)
duplicate_tuple = (1, 2, 3)

print("\nФиксированный порядок элементов кортежа:")
print(
    "Кортежи:",
    original_tuple,
    shuffled_tuple,
    "равны?",
    original_tuple == shuffled_tuple,
)
print(
    "Кортежи:",
    duplicate_tuple,
    original_tuple,
    "равны?",
    duplicate_tuple == original_tuple,
)

print("\nОбращение к элементам кортежа по индексу:")
print("Кортеж:", fruits_tuple)
print("Элемент с индексом 2:", fruits_tuple[2])
print("Элемент с индексом -3:", fruits_tuple[-3])
print("Элементы с индексами 0:3:", fruits_tuple[0:3])

print("\nКортеж допускает дублирование элементов:")
print(
    "Кортеж:", fruits_tuple,
    "\nЭлемент с индексом 0 равен элементу с индексом 4 ? ",
    fruits_tuple[0] == fruits_tuple[4],
)

print("\nКортеж не изменяемый, но его можно преобразовать в список:")

# преобразование кортежа в список
fruits_list = list(fruits_tuple)
print("Список:", fruits_list)

print("Добавим в список элемент 'strawberry' и преобразуем в кортеж:")
# добавление нового элемента списка
fruits_list.append('strawberry')

# преобразование списка в кортеж
fruits_tuple = tuple(fruits_list)

print("Кортеж:", fruits_tuple)

print("\nОбъединение кортежей:")
print("Добавим к кортежу:", fruits_tuple)
print("Кортеж содержащий: cherry, pineapple")
# Кортежи не изменяемые!
# Создаётся новый кортеж, который заменяет старый:
fruits_tuple = fruits_tuple + ('cherry', 'pineapple')
print("Новый кортеж:")
print(fruits_tuple)

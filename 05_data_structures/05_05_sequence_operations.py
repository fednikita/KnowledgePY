"""Структуры данных — операции с последовательностями."""
"""Некоторые операции применяются ко всем последовательностям:"""

print("Итерации с использованием цикла for")
fruits = ['apple', 'peach', 'strawberry', 'pineapple']
print("Перебор элементов списка:", fruits)
for fruit in fruits:
    print(fruit)


print("\nПреобразование типов")

list_letters = ['a', 'b', 'c']
print("Список:", list_letters)

tuple_letters = tuple(list_letters)
print("Кортеж:", tuple_letters)

set_letters = set(list_letters)
print("Множество:", set_letters)

print("\nУмножение *")

print('Умножение списка на 3:', list_letters)
multiple_letters = list_letters * 3
print('Результат:', multiple_letters)

print("\nПроверка принадлежности, оператор in:")

print("b принадлежит", tuple_letters, "?", 'b' in tuple_letters)
print("d принадлежит", tuple_letters, "?", 'd' in tuple_letters)


print("\nПодсчёт количества вхождений, count:")
print(multiple_letters)
print('b входит', multiple_letters.count('b'), 'раз(а)')

print("\nПолучение индекса элемента, index:")
print(multiple_letters)
print('Индекс элемента b: ', multiple_letters.index('b'))
# Если элемент встречается более 1 раза, возвращается индекс первого вхождения

print("\nПодсчёт количества элементов, len:")
print(multiple_letters)
print("Количество элементов:", len(multiple_letters))

numbers = (5, 3, 10, 7, 9)
print("\nПоиск максимального значения, max:")
print(numbers)
print("Максимальное значение:", max(numbers))

print("\nПоиск минимального значения, min:")
print(numbers)
print("Максимальное значение:", min(numbers))

print("\nСумма всех значений, sum:")
print(numbers)
print("Сумма:", sum(numbers))
# Должны быть только целые числа

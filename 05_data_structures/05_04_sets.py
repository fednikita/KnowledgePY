"""Структуры данных — множества."""
""" Множества изменяемы

Множества это неупорядоченная коллекция уникальных элементов:
Неупорядоченные
Неиндексируемые
Нет дубликатов
Нет изменяемых типов

Множества допускают использование только хэшируемых элементов.

Поскольку кортежи неизменяемы их можно хранить в множествах.
"""

print("Основы множеств")
empty = set()  # Пустое множество.
# set() обозначает пустое множество, {} используются не только для множеств
fruits = {'apple', 'banana', 'peach', 'strawberry'}  # Элементы одного типа
fruits_mixed = {'banana', 'strawberry', 'apple', 'peach'}
different = {'text', 23, 3.14, 9.20, False}  # Элементы разных типов

print("Множества неупорядоченны")
print("Вывод множества 'apple', 'banana', 'peach', 'strawberry':", fruits)

print(
    "Множество",
    fruits,
    "и множество",
    fruits_mixed,
    "равны?",
    fruits == fruits_mixed,
)
# Результат true

print("\nОперации с элеменатми множеств")
print("Добавление элемента cherry в множество fruits")
fruits.add('cherry')
print(fruits)

print("\nУдаление элемента cherry")
fruits.remove('cherry')
print("Результат:", fruits)

print("\nУдаление случайного элемента")
print("Удаляемый элемент:", fruits.pop())
print("Результат:", fruits)

print("\nУдаление всех элементов fruits")
fruits.clear()
print("Результат:", fruits)


print("\nОперации над множествами")
fruits = {'grape', 'apple', 'strawberry', 'cherry'}
print("Объединение множеств:")
print(fruits)
print(fruits_mixed)

fruits_union = fruits.union(fruits_mixed)
print("Результат:", fruits_union)

print("\nПересечение множеств:")
fruits_and = fruits & fruits_mixed
print("Оператор &:", fruits_and)

fruits_and = fruits.intersection(fruits_mixed)
print("Используя intersection:", fruits_and)

fruits.intersection_update(fruits_mixed)
print("Используя intersection_update:", fruits)

print("\nРазность множеств:")
print(fruits_union)
print(fruits_and)
fruits_difference = fruits_union - fruits_and
print("Оператор -:", fruits_difference)

fruits_difference = fruits_union.difference(fruits_and)
print("Используя set.difference:", fruits_difference)

fruits_difference.intersection_update(fruits_mixed)
print("Используя intersection_difference:", fruits_difference)

print("\nСимметричная разность множеств XOR:")
print(fruits_mixed)
print(fruits_union)
fruits_symmetric = fruits_mixed ^ fruits_union
print("Оператор ^:", fruits_symmetric)

fruits_symmetric = fruits_mixed.symmetric_difference(fruits_union)
print("Используя set.symmetric_difference:", fruits_symmetric)

fruits_union.symmetric_difference_update(fruits_mixed)
print("Используя symmetric_difference_update:", fruits_union)

print("\nНе пересекающиеся множества:")

print(
    "Множество:",
    fruits,
    "\nМножество:",
    fruits_difference,
    "\nНепересекаются?",
    fruits.isdisjoint(fruits_difference))

print("\nПодмножества:")

print(
    "Множество:",
    fruits,
    "\nЯвляется подмножеством:",
    fruits_mixed,
    "\n?",
    fruits.issubset(fruits_mixed))

print("\nНадмножества:")

print(
    "Множество является надмножеством?:",
    fruits_mixed,
    "\nМножества:",
    fruits,
    "\n",
    fruits_mixed.issuperset(fruits))

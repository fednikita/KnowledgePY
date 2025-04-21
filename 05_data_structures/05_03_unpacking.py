"""Структуры данных — распаковка."""
# Распаковка применима к любым последовательностям: списки, кортежи и т.д.

print("Распаковка кортежа:")
employee = ('Ivan', 23)
print(employee)
# Количество переменных должно соответствовать количеству элементов
name, age = employee
print("Результат распаковки:", name, age)

print("\nРаспаковка кортежа используя оператор * в конце:")
name, age, *roles = ('Vasya', 18, 'Developer', 'Tester')
print(name, "тип:", type(name))
print(age, "тип:", type(age))
# оставшиеся элементы заносятся в список
print(roles, "тип:", type(roles))

print("\nРаспаковка кортежа используя оператор * в начале:")
*roles, name, age = ('Developer', 'Tester', 'Vasya', 18)
# если * в начале, распаковка начинается с конца
print(name, "тип:", type(name))
print(age, "тип:", type(age))
print(roles, "тип:", type(roles))

print("\nРаспаковка кортежа используя оператор * в середине:")
name, *roles, age = ('Vasya', 'Developer', 'Tester', 18)
# если * в середине, распаковка начинается из начала и конца
# средние значения заносятся в список
print(name, "тип:", type(name))
print(age, "тип:", type(age))
print(roles, "тип:", type(roles))

print("\nРаспаковка аргументов функции:")


def multiply(a, b):
    return a * b


params = (5, 3)  # кортеж с 2 элементами
# * перед params распаковывает кортеж в отдельные аргументы
# аналогично вызову myltiply(5, 3)
""" количество элементов в распаковываемом объекте
должно совпадать с количеством параметров функции """
print(multiply(*params))

print("\nРаспаковка возвращаемых значений функции:")


def divide(n, m):
    return n / m, n % m
# функция возвращает кортеж из двух элементов


result, remainder = divide(5, 2)
print(result)
print(remainder)

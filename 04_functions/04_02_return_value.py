"""Основы функций - возвращаемое значение."""

print(f"Пример функции возвращающей True || False:")
# return - завершающий оператор функции.


def test(numbers):
    if numbers == "123":
        return True
    # else: не нужен!
    return False


print(test("123"))
print(test("01234"))

print(f"Функция не имеющая return:")


def nothing(name):
    print(f"Hello, {name}!")


result = nothing("Viktor")
# Функция не имеет return, поэтому результат выполнения функции None
print(result)


# Важно! Не путать возращаемое значение и печать из функции.

print(f"Функция печатающая текст:")


def print_value():
    print(f"Hello world!")


print_value()

print(f"Функция возвращающая текст:")


def return_value():
    return f"Hello world!"


print(return_value())


print(f"Функция возвращающая два значения:")


def divide_and_remainder(n1, n2):
    return n1 / n2, n1 % n2


values = divide_and_remainder(5, 2)

print(f"Частное: {values[0]}")
print(f"Остаток: {values[1]}")

# Возвращаемые значения хранятся в виде кортежа их можно распаковать:

quotient, remainder = divide_and_remainder(5, 2)
print("Частное:", quotient)
print("Остаток:", remainder)

print(f"Функция возвращающая функцию:")


def factor(a):  # Принимает аргумент и возвращает функцию inner
    def inner(b):
        return a * b

    return inner


# Функция factor возвращает inner со значением a, в примере равный 2
# Пример doubler, принимает аргумент и умножает его на a
doubler = factor(2)

# Пример tripler работает аналогично
tripler = factor(3)

print(doubler(20))  # doubler(20) -> inner(20) с a = 2 -> 2*20 -> 40
print(tripler(20))  # tripler(20) -> inner(20) с a = 3 -> 3*20 -> 60

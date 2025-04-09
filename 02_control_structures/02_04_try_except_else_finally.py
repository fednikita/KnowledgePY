"""Управляющие структуры — try except else finally."""

"""
Допустимый порядок использования блоков try except else finally:
try except
try except else
try except else finally
try except finally
try finally
"""

print(f"Проверка деления на 0:")
n1 = int(input('Введите делимое: '))
n2 = int(input('Введите делитель: '))

try:
    print("Частное =", n1 / n2)
except ZeroDivisionError:  # Проверка деления на 0
    print('Делитель не может быть равно нулю!')

print(f"\nПроверка деления на 0 и введения не числового значения:")
print(f"Обработка нескольких ошибок в одном try, несколько except:")
try:
    n1 = int(input('Введите делимое: '))
    n2 = int(input('Введите делитель: '))
    print("Частное =", n1 / n2)
except ZeroDivisionError:
    print('Делитель не может быть равно нулю!')
except ValueError:  # Проверка введения корректного типа данных.
    print('Введите целое число!')

print(f"\nОбработка ошибок отдельно, несколько try-except:")

try:
    n1 = int(input('Введите делимое: '))
    n2 = int(input('Введите делитель: '))
except ValueError:
    print('Введите целое число!')

try:
    print("Частное =", n1 / n2)
except ZeroDivisionError:
    print('Делитель не может быть равно нулю!')

print(f"\nОбработка нескольких исключений, один except:")

try:
    n1 = int(input('Введите делимое: '))
    n2 = int(input('Введите делитель: '))
    print("Частное =", n1 / n2)
except (ZeroDivisionError, ValueError):
    print('Ошибка')  # Не информативно

print(f"\nОбработка нескольких исключений, один except, использование as:")
# Обработка нескольких исключений, один except
# as присваивает ошибку переменной.
# isinstance() встроенная функция для проверки,
# является ли объект экземпляром определённого типа.

try:
    n1 = int(input('Введите делимое: '))
    n2 = int(input('Введите делитель: '))
    print("Частное =", n1 / n2)
except (ZeroDivisionError, ValueError) as error:
    if isinstance(error, ZeroDivisionError):
        print('Делитель не может быть равно нулю!')
    elif isinstance(error, ValueError):
        print('Введите целое число!')
"""
except без указания определённых исключений,
bare except - перехватывают любые возникшие исключения.
Включая системные (Ctrl+C sys.exit() и т.д.)
Не рекомендуется использовать!

Пример:
n1 = int(input('Введите делимое: '))
n2 = int(input('Введите делитель: '))
try:
    print("Частное =", n1 / n2)
except:
    print('Ошибка')
"""
print(f"\nПроверка деления на любые ошибки, Exception:")
# Лучше использовать базовый класс Exception для проверки на все исключения

try:
    n1 = int(input('Введите делимое: '))
    n2 = int(input('Введите делитель: '))
    print("Частное =", n1 / n2)
except ValueError:
    print('Введите целое число!')
except ZeroDivisionError:
    print('Делитель не может быть равно нулю!')
except Exception as err:
    print(f'Ошибка: {err}')

print(f"\nПроверка деления на 0, try except else:")

n1 = int(input('Введите делимое: '))
n2 = int(input('Введите делитель: '))

try:
    print("Частное =", n1 / n2)
except ZeroDivisionError:
    print('Делитель не может быть равно нулю!')
else:  # если ошибок нет, выполняется else
    print('Деление успешно завершено!')

print(f"\nПроверка деления на 0, try except finally:")

n1 = int(input('Введите делимое: '))
n2 = int(input('Введите делитель: '))

try:
    print("Частное =", n1 / n2)
except ZeroDivisionError:
    print('Делитель не может быть равно нулю!')
finally:  # Выполняется в любом случае
    print('Программа завершена')

print(f"\nПроверка деления на 0, try finally:")

n1 = int(input('Введите делимое: '))
n2 = int(input('Введите делитель: '))

try:
    print("Частное =", n1 / n2)
finally:  # Выполняется в любом случае
    print('Программа завершена')
# без except, после выполнения finally программа завершится с ошибкой

print(f"\nПроверка деления на любые ошибки, try except else finally:")

try:
    n1 = int(input('Введите делимое: '))
    n2 = int(input('Введите делитель: '))

    print("Частное =", n1 / n2)

except ValueError:
    print('Введите целое число!')

except ZeroDivisionError:
    print('Делитель не может быть равно нулю!')

except Exception as err:
    print(f'Ошибка: {err}')
else:
    print('Деление успешно завершено!')

finally:
    print('Программа завершила работу.')

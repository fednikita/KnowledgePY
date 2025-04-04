"""Основы функций - область видимости."""

print(f"Пример глобальной области видимости:")

var = 41  # Глобальная переменная


def show_var():  # Глобальная функция
    print(f"Доступ к переменной из внутренней функции: {var}")


print(f"Доступ к переменной из внешней функции: {var}")
show_var()

print(f"\nПримеры изменения глобальной переменной:")


def update_var_global():
    # Для изменения глобальной переменной необходимо указать global:
    global var
    var = var + 1


update_var_global()
print(f"Изменение глобальной переменной внутри функции: {var}")


# Лучше не использовать global, например:
def update_var_function(var):  # var для примера!
    var = var + 1  # локальная переменная
    return var


var = update_var_function(var)
# присвоим переменной результат выполнения функции
print(f"Изменение глобальной переменной без global: {var}")

print(f"\nПримеры включающей области видимости:")

print(f"Вызов вложенной функции внутри функции:")


def outer():
    var = 44

    def inner():
        print(var)
        # аналогично global переменная доступна, но не может быть обновлена
    inner()  # Вызываем inner внутри outer


outer()  # Вызываем outer, выведет: 44

print(f"Возврат вложенной функции:")


def outer():
    var = 45

    def inner():
        print(var)

    return inner()  # Возвращаем функцию inner


outer()  # Вызываем outer, выведет: 45


print(f"Вложенная функция nonlocal переменная:")


def outer():
    var = 45

    def inner():
        nonlocal var  # без nonlocal будет создана новая переменная
        # nonlocal изменяет переменную из ближайшей внешней области видимости
        var = var + 1

    print('До вызова вложенной функции:', var)
    inner()
    print('После вызова вложенной функции:', var)


outer()

"""Основы функций."""

print(f"Функция без аргументов:")
def hello():  # <имя функции>(<параметры функции>):
    print('Hello, World!')  # <тело функции>

hello()    # вызов функции

print(f"Функция с аргументом:")
def hello_name(name):
    print(f'Hello, {name}!')

name = input("Введите ваше имя: ")
hello_name(name)  # аргументы функции

print(f"Функция с аргументом по умолчанию:")
def hello_name(name='World'):  # параметр по умолчанию
    print(f'Hello, {name}!')
hello_name()
hello_name(name)

print(f"Функция с позиционными аргументами:")
logic = bool(input(
    "Введите любой символ(True) или нажмите Enter (False):"
    ))
def hello_true(name, logical):
    if logical:
        print(f'Hello, {name}, True!')
    else:
        print(f'Hello, {name}, False!')

# Позиционные аргументы
hello_true(name, logic)
# Первый аргумент позиционный, второй ключевой
hello_true('Vasya', logical=False)
# Ключевые аргументы, порядок не важен
hello_true(logical=True, name='Petya')

print(f"Вариативные позиционные аргументы:")
def hello_names(*names):
    for name in names:
        print(f'Hello, {name}!')

hello_names('Vasya', 'Ivan', 'Alex')
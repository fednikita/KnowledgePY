"""Основы функций."""

print(f"Функция без аргументов:")


def hello():  # <имя функции>(<параметры функции>):
    print("Hello, World!")  # <тело функции>


hello()  # вызов функции

print(f"Функция с аргументом:")


def hello_name(name):
    print(f"Hello, {name}!")


name = input("Введите ваше имя: ")
hello_name(name)  # аргументы функции

print(f"Функция с аргументом по умолчанию:")


def hello_name(name="World"):  # параметр по умолчанию
    print(f"Hello, {name}!")


hello_name()
hello_name(name)

print(f"Функция с позиционными аргументами:")
logic = bool(input("Введите любой символ(True) или нажмите Enter (False):"))


def hello_true(name, logical):
    if logical:
        print(f"Hello, {name}, True!")
    else:
        print(f"Hello, {name}, False!")


# Позиционные аргументы
hello_true(name, logic)
# Первый аргумент позиционный, второй ключевой
hello_true("Vasya", logical=False)
# Ключевые аргументы, порядок не важен
hello_true(logical=True, name="Petya")

print(f"Функция с переменными позиционными аргументами:")


#  * означает переменное количество принимаемых параметров
def hello_names(*names):  # Принимает кортеж значений
    for name in names:
        print(f"Hello, {name}!")


hello_names("Vasya", "Ivan", "Alex")

print(f"Функция с переменным количеством аргументов:")


# Ключевые аргументы обрабатываются как словарь, ключ - значение
# ** означает переменное количество ключевых параметров
def variadic_names(**args):
    print(args["arg1"])
    print(args["arg2"])


variadic_names(arg1="Vasya", arg2="Ivan", arg3="Alex")

print(f"Функция со смешанными аргументами:")


# Позиционные аргументы всегда ставятся перед ключевыми!
def mixing_arguments(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(kwargs["arg1"])
    print(kwargs["arg2"])


mixing_arguments("Vasya", "Ivan", "Alex", arg1="Viktor", arg2="Oleg")

print(f"Функция с переменным количеством и обычными аргументами:")


# Если функция принимает переменное количество параметров и обычные аргументы
# Обычные аргументы передаются как ключевые!
def variadic_normal(*args, normal_arg, normal_arg2):
    print(normal_arg)
    print(normal_arg2)


variadic_normal(
    "Vasya", "Ivan", "Alex", normal_arg="Viktor", normal_arg2="Oleg"
)

print(f"Функция с только позиционными аргументами:")


# Параметры принимающие только позиционные аргументы размещаются до /
# После / параметры принимают как ключевые так и позиционные аргументы.
def positions_only(pos_only, /, normal_arg, normal_arg2):
    print(f"{pos_only} {normal_arg}! \n{pos_only} {normal_arg2}!")


positions_only("Hello", normal_arg="Viktor", normal_arg2="Oleg")

print(f"Функция с только ключевыми аргументами:")


# Параметры принимающие позиционные и ключевые аргументы указываются до *
# После * параметры принимают только позиционные аргументы.
def key_only(normal, *, kwarg1, kwarg2):
    print(f"{normal} {kwarg1}! \n{normal} {kwarg2}!")


key_only("Hello", kwarg1="Viktor", kwarg2="Oleg")

print(f"Функция с только позиционными, любыми и только ключевыми аргументами:")


# Можно использовать / * одновременно:
def both_arg(pos_only, /, normal, *, kwarg):
    print(f"{pos_only}{normal}{kwarg}")


both_arg("Hello ", "World", kwarg="!")

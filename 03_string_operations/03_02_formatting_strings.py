"""Операции со строками — форматирование строк."""

string1 = "Hello"
string2 = "world"

# Изменение регистра строк
print("Верхний регистр: ", string2.upper())
print("Нижний регистр: ", string2.lower())
print("Первый символ в верхний регистр: ", string2.capitalize())
# преобразует все символы верхнего регистра в нижний регистр
# все символы нижнего регистра в символы верхнего регистра
print("Противоположный регистр: ", string2.swapcase())
# Первый символ каждого слова в строке в верхний регистр
print("Первый символ в верхний регистр: ", string2.title())

# Методы проверки
print("Проверка строки: ", string1)
print("Все символы буквы алфавита: ", string1.isalpha())
print("Все символы буквенно-цифровые: ", string1.isalnum())
print("Все символы цифры или целые числа: ", string1.isdigit())
print("Может быть именем переменной: ", string1.isidentifier())
print("Все ли символы в строке строчные: ", string1.islower())
print("Все символы в строке числа: ", string1.isnumeric())
print("Все символы в строке пробелы: ", string1.isspace())
print("Все слова в строке начинаются с заглавной буквы: ", string1.istitle())
print("Все символы заглавные: ", string1.isupper())

# Объединение строк (конкатенация)
string3 = string1 + " " + string2  # важен порядок, это не сложение чисел
print(string3)
print(string1 + " " + string2)  # аналогично

# Метод join(), принимает список строк, возвращает одну строку
string3 = " ".join([string1, string2])
print(string3)

# строки можно объединять только со строками
integer = 8
print(string1 + str(integer))

# Замена или удаление символов из строки, метод replace
string3 = string3.replace(string2, "")  # (, удаление)
print(string3)
string3 = string3.replace(string1, string2)  # (что заменить, на что заменить)
print(string3)

# Дублирование (умножение) строки
# * Повторяет содержимое переменной заданное число раз
stringsum = (string1 + " ") * 3
print(stringsum)

# count() функция подсчитывает количество появлений подстроки в строке
print(
    "Слово Hello встречается",
    stringsum.count("Hello"),
    "раза в строке",
    stringsum,
)

# Функции str.startswith() & str.endswith()
# Проверка начинается или заканчивается строка с заданной строки
print(
    "Строка",
    string1,
    ' начинается со строки "Hello" ?',
    string1.startswith("Hello"),
)
print(
    "Строка",
    string1,
    ' заканчивается строкой "world" ?',
    string1.endswith("world"),
)

# Метод format() включает значения переменных в строку
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")

age = int(input("Введите ваш возраст: "))
# format автоматически приведёт любой тип данных к строке

# {} заменяется аргументами функции
# аргументы функции format автоматически преобразуются в строку
print("Здравствуйте {} {} вам {} лет".format(surname, name, age))
# {} порядок подстановки можно указать по индексу аргумента
print("Здравствуйте {1} {0} вам {2} лет".format(name, surname, age))

# Именованные заполнители Named placeholders
# По аналогии с заполнением по индексу
template = "Здравствуйте {your_surname} {your_name} вам {your_age} лет"
print(template.format(your_surname=surname, your_name=name, your_age=age))

# f строки
# f строка как и format автоматически приведёт любой тип данных к строке
print(f"Здравствуйте {surname} {name} вам {age} лет")

# len() функция, возвращает длину любой последовательности
length = len(name)
print(f"Количество символов в вашем имени: {length}")

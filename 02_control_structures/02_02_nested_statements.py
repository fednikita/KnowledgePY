"""Управляющие структуры — вложенные операторы."""

age = int(input("Введите ваш возраст: "))
driving_test_score = int(input("Введите количество штрафных баллов: "))

if age >= 18:  # Можно писать операторы if внутри операторов if.
    if driving_test_score < 7:
        print(
            "Вы старше 18 лет и успешно сдали экзамен по вождению, вы можете получить права."
        )
    else:
        print("Вы не сдали экзамен по вождению, вы не можете получить права.")
else:
    print("Вы не можете водить, вам нет 18 лет.")

if age > 18:
    print("Вы старше 18 лет.")
elif age < 18:  # Cокращение от else: if
    print("Вы младше 18 лет.")
else:
    print("Вам 18 лет.")

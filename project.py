while True:
    print("\n===== КАЛЬКУЛЯТОР =====")
    print("1 - Сложение (+)")
    print("2 - Вычитание (-)")
    print("3 - Умножение (*)")
    print("4 - Деление (/)")
    print("5 - Целочисленное деление (//)")
    print("6 - Остаток от деления (%)")
    print("7 - Возведение в степень (**)")
    print("8 - Сравнение чисел")
    print("9 - Логические операции")
    print("10 - Проверка принадлежности")
    print("11 - Проверка тождественности")
    print("0 - Выход")

    choice = input("Выберите операцию: ")

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "1":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print("Результат:", a + b)

    elif choice == "2":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print("Результат:", a - b)

    elif choice == "3":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print("Результат:", a * b)

    elif choice == "4":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        if b == 0:
            print("Ошибка: на ноль делить нельзя!")
        else:
            print("Результат:", a / b)

    elif choice == "5":
        a = int(input("Введите первое целое число: "))
        b = int(input("Введите второе целое число: "))

        if b == 0:
            print("Ошибка: на ноль делить нельзя!")
        else:
            print("Результат:", a // b)

    elif choice == "6":
        a = int(input("Введите первое целое число: "))
        b = int(input("Введите второе целое число: "))

        if b == 0:
            print("Ошибка: на ноль делить нельзя!")
        else:
            print("Результат:", a % b)

    elif choice == "7":
        a = float(input("Введите число: "))
        b = float(input("Введите степень: "))
        print("Результат:", a ** b)

    elif choice == "8":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        print("a == b:", a == b)
        print("a != b:", a != b)
        print("a > b:", a > b)
        print("a < b:", a < b)
        print("a >= b:", a >= b)
        print("a <= b:", a <= b)

    elif choice == "9":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        print("a > 0 and b > 0:", a > 0 and b > 0)
        print("a > 0 or b > 0:", a > 0 or b > 0)
        print("not (a > 0):", not (a > 0))

    elif choice == "10":
        number = input("Введите число: ")

        numbers = ["1", "2", "3", "4", "5"]

        print("Список:", numbers)
        print("number in list:", number in numbers)
        print("number not in list:", number not in numbers)

    elif choice == "11":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        first = [a]
        second = first
        third = [b]

        print("first is second:", first is second)
        print("first is not third:", first is not third)

    else:
        print("Ошибка: такой операции нет.")
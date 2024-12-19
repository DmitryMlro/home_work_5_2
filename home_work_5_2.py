while True:
    first_num = int(input("Введіть перше число: "))
    math_operation = input("Вкажіть операцію (+, -, *, /): ")
    second_num = int(input("Введіть друге число: "))

    if math_operation == "+":
        print("Відповідь:", first_num + second_num)
    elif math_operation == "-":
        print("Відповідь:", first_num - second_num)
    elif math_operation == "*":
        print("Відповідь:", first_num * second_num)
    elif math_operation == "/" and second_num != 0:
        print("Відповідь:", first_num / second_num)
    else:
        print("Дані введено некоректно, або дільник дорівнює 0")

    turn_calc = input("Для продовження натсність - у: ").lower()
    if turn_calc not in ("y"):
        print("Завершення роботи")
        break

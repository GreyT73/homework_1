number = int(input("Введите трехзначное число: "))
if 100 < number < 1000:
    first_digit = number % 10
    second_digit = number // 10 % 10
    third_number = number // 100
    print("Сумма цифр в числе ", number, "равна ", first_digit + second_digit + third_number)
    print(first_digit, second_digit, third_number)
else:
    print("Введенное число не трехзначное")

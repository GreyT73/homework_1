while True:
    number = int(input("Введите шестизначное число: "))
    if 99999 < number < 1000000:
        first_digit =  number % 10
        second_digit = number // 10 % 10
        third_digit = number // 100 % 10
        fourth_digit = number // 1000 % 10
        fifth_digit = number // 10000 % 10
        sixth_digit = number // 100000
        if first_digit + second_digit + third_digit == fourth_digit + fifth_digit + sixth_digit:
            print(number, "является счастливым билетом")
        else:
            print(number, "НЕ является счастливым билетом")
        break
    else:
        print("Это не шестизначное число")


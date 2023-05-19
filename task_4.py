while True:
    cranes = int(input("Введите число кратное 6: "))
    if cranes % 6 == 0:
        boy = cranes / 6
        boy = int(boy)
        girl = (boy + boy) * 2
        print("Петя сделал", boy, "журавликов, Катя сделала", girl, "журавликов, а Сережа", boy, "журавликов")
        break
    else:
        print("По условиям задачи ребята не могли сделать столько журавликов. Число должно быть кратно 6")


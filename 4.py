while True:
    name = input('Пожалуйста введите целое положительное число  ')
    while name.isdigit() != True:
        print("Вы ввели значение неверно, попробуйте еще раз")
        name = input('Пожалуйста введите целое положительное число  ')
    name = int(name)
    mmax = 0
    List = 10
    name1 = name
    while List >= 1:
        name2 = int(name1 % 10)
        List = name1 // 10
        if mmax < name2:
            mmax = name2
        # print(mmax)
        name1 = List
    print('Максимальная цифра в числе', name, ":", mmax)
    ex = int(input('Если хотите продолжить, нажмите 1, если нет-другую цифру  '))
    if ex != 1:
        break

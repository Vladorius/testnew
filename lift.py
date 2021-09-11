current_floor = 3   # текущее положение кабины лифта
floors = 9          # количество этажей
lift_condition = False
buttons_out_cabin_list = []  # список с номерами кнопок нажатых на вызов лифта на этажах
buttons_in_cabin_list = []   # список с номерами кнопок нажатых внутри лифта
count_people_in_lift = 0

while True:
    if not lift_condition:   # Если лифт свободен
        if len(buttons_out_cabin_list) == 0:  # проверка нет ли вызова лифта на других этажах
            F_xx = int(input('На каком этаже вызвать лифт? '))
            buttons_out_cabin_list.append(F_xx)

        if F_xx < current_floor:
            for i in range(current_floor, int(F_xx)-1, -1):
                if i == current_floor:
                    print(f'Лифт был вызван на {F_xx}-м этаже и начал движение вниз с {current_floor}-го.')
                elif i != F_xx:
                    print(f'Лифт проезжает мимо {i}-го этажа вниз. '
                          f'Есть ли действия на других этажах? Да/Нет', end=' ')
                    act = input()
                    if act == "Да":
                        push_button = input('Введите через запятую этажи, на которых вызывают лифт: ').split(",")
                        for button in range(len(push_button)):
                            buttons_out_cabin_list.append(int(push_button[button]))
                else:
                    print(f'\nДвери лифта открылись на {F_xx}-м этаже.')
                    buttons_out_cabin_list.remove(i)
        elif F_xx > current_floor:
            for i in range(current_floor, int(F_xx) + 1):
                if i == current_floor:
                    print(f'Лифт был вызван на {F_xx}-м этаже и начал движение вверх с {current_floor}-го.')
                elif i != F_xx:
                    print(f'Лифт проезжает мимо {i}-го этажа вверх. '
                          f'Есть ли действия на других этажах? Да/Нет', end=' ')
                    act = input()
                    if act == "Да":
                        push_button = input('Введите через запятую этажи, на которых вызывают лифт: ').split(",")
                        for button in range(len(push_button)):
                            buttons_out_cabin_list.append(int(push_button[button]))
                else:
                    print(f'\nДвери лифта открылись на {F_xx}-м этаже.')
                    buttons_out_cabin_list.remove(i)
        C_xx = int(input(f'Человек зашел в лифт и нажал кнопку этажа №'))
        count_people_in_lift += 1
        print("\nКоличество людей в лифте:", count_people_in_lift)
        buttons_in_cabin_list.append(C_xx)     # нажатые кнопки в лифте
        current_floor = F_xx
        lift_condition = True
        continue

    elif lift_condition:        # Если в лифте есть люди

        if C_xx > current_floor:
            print('Двери закрываются. Лифт начинает движение вверх')
            for f in range(current_floor, C_xx+1):
                if f == current_floor:
                    print(f'\nЛифт был вызван на {C_xx}-м этаже и '
                          f'начал движение вверх с {current_floor}-го этажа.')
                elif f != C_xx:
                    print(f'Лифт проезжает мимо {f}-го этажа вверх. '
                          f'Есть ли действия на других этажах? Да/Нет', end=' ')
                    act = input()
                    if act == "Да":
                        push_button = input('Введите через запятую этажи, на которых вызывают лифт: ').split(",")
                        for button in range(len(push_button)):
                            # добавление в список нажатых кнопок на этажах
                            buttons_out_cabin_list.append(int(push_button[button]))
                    if f in buttons_out_cabin_list:
                        print('На этом этаже была нажата кнопка вызова. Дверь открывается.')
                        buttons_out_cabin_list.remove(f)
                        if count_people_in_lift < 3:      # проверка на загруженность лифта
                            c_xx = int(input(f'Человек зашел в лифт и нажал кнопку этажа № '))
                            buttons_in_cabin_list.append(c_xx)
                            count_people_in_lift += 1
                        else:
                            print('Лифт переполнен. Максимум 3 человека. Двери закрываются.')
                    if f in buttons_in_cabin_list:
                        print(f'Лифт останавливается на {f}-м этаже. Пассажир выходит.')
                        buttons_in_cabin_list.remove(f)
                        count_people_in_lift -= 1
                        print(count_people_in_lift)
                        if count_people_in_lift == 0:
                            lift_condition = False
                            continue
                elif f == C_xx:
                    print(f'Двери лифта открылись на {C_xx}-м этаже. Пассажир выходит.')
                    buttons_in_cabin_list.remove(f)
                    count_people_in_lift -= 1
                    current_floor = f
                    if len(buttons_in_cabin_list) != 0:
                        C_xx = buttons_in_cabin_list[0]
                    else:
                        lift_condition = False
                        F_xx = buttons_out_cabin_list[0]

        elif C_xx < current_floor:
            print('Двери закрываются. Лифт начинает движение вниз.')
            for f in range(current_floor, int(C_xx) - 1, -1):
                if f == current_floor:
                    print(f'Лифт был вызван на {C_xx}-м этаже и '
                          f'начал движение вниз с {current_floor}-го этажа.')
                elif f != C_xx:
                    print(f'\nЛифт проезжает мимо {f}-го этажа вниз. '
                          f'Есть ли действия на других этажах? Да/Нет', end=' ')
                    act = input()
                    if act == "Да":
                        push_button = input('Введите через запятую этажи, на которых вызывают лифт: ').split(",")
                        for button in range(len(push_button)):
                            # добавление в список нажатых кнопок на этажах
                            buttons_out_cabin_list.append(int(push_button[button]))
                    if f in buttons_out_cabin_list:
                        print('На этом этаже была нажата кнопка вызова. Дверь открывается.')
                        buttons_out_cabin_list.remove(f)
                        print("Количество людей в лифте:", count_people_in_lift)
                        if count_people_in_lift < 3:  # проверка на загруженность лифта
                            c_xx = int(input(f'Человек зашел в лифт и нажал кнопку этажа № '))
                            buttons_in_cabin_list.append(c_xx)
                            count_people_in_lift += 1
                        else:
                            print('Лифт переполнен. Максимум 3 человека. Двери закрываются.')
                    if f in buttons_in_cabin_list:
                        print(f'\nЛифт останавливается на {f}-м этаже. Пассажир выходит.')
                        buttons_in_cabin_list.remove(f)
                        count_people_in_lift -= 1
                elif f == C_xx:
                    print(f'Двери лифта открылись на {C_xx}-м этаже. Пассажир выходит.')
                    buttons_in_cabin_list.remove(f)
                    count_people_in_lift -= 1
                    current_floor = f

                    if len(buttons_in_cabin_list) != 0:
                        C_xx = buttons_in_cabin_list[0]
                    else:
                        lift_condition = False
                        F_xx = buttons_out_cabin_list[0]

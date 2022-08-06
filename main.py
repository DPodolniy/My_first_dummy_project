from random import randint, choice


def passwordscreen():  # функция защитного экрана
    difficulty = 4
    # difficulty = randint(4,6) ## рандомный выбор сложности в разработке
    symbolpool = ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '()']  # 11 символов для визуального шума
    # 50 слов для пароля
    wordpool4 = ['ALOE', 'ACID', 'BALD', 'BABY', 'CAFE', 'CUNT', 'DEAD', 'DICE', 'EACH', 'ECHO', 'FOAM', 'FONT', 'GAIN',
                 'GOOD', 'HALF', 'HAND', 'ISLE', 'ITEM', 'JAZZ', 'JUNE', 'KHAN', 'KISS', 'LADY', 'LIKE', 'MAIL', 'MASK',
                 'NAIL', 'NICE', 'OILY', 'ONYX', 'PAIN', 'POOL', 'QAZI', 'QUAD', 'RACE', 'RAIL', 'SACK', 'SOAP', 'TABU',
                 'TACT', 'UGLY', 'UNIT', 'VAIN', 'VASE', 'WAGE', 'WAIT', 'YARD', 'YOGA', 'ZERO', 'ZETA']
    # создаем пустые пулы, которые будут выстпупать в роли строк консоли
    passwordpool1, passwordpool2, passwordpool3, passwordpool4, passwordpool5 = [], [], [], [], []
    passwordpool6, passwordpool7, passwordpool8, passwordpool9, passwordpool10 = [], [], [], [], []
    if difficulty == 4:
        while len(passwordpool1) < 75:  # Создаем пять строк с символами визуального шума
            passwordpool1.append(choice(symbolpool))
        while len(passwordpool2) < 75:
            passwordpool2.append(choice(symbolpool))
        while len(passwordpool3) < 75:
            passwordpool3.append(choice(symbolpool))
        while len(passwordpool4) < 75:
            passwordpool4.append(choice(symbolpool))
        while len(passwordpool5) < 75:
            passwordpool5.append(choice(symbolpool))
        while len(passwordpool6) < 75:
            passwordpool6.append(choice(symbolpool))
        while len(passwordpool7) < 75:
            passwordpool7.append(choice(symbolpool))
        while len(passwordpool8) < 75:
            passwordpool8.append(choice(symbolpool))
        while len(passwordpool9) < 75:
            passwordpool9.append(choice(symbolpool))
        while len(passwordpool10) < 75:
            passwordpool10.append(choice(symbolpool))
        global pass_word
        pass_word = choice(wordpool4)  # выбираем пароль из пула
        real_passwordpool = randint(1, 10)  # выбираем строку для иньекции пароля
        if real_passwordpool == 1:
            passwordpool1[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4) # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 2:
            passwordpool2[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4) # выбираем фальшивое слово
            passwordpool1[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 3:
            passwordpool3[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 4:
            passwordpool4[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 5:
            passwordpool5[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 6:
            passwordpool6[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 7:
            passwordpool7[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 8:
            passwordpool8[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 9:
            passwordpool9[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 10:
            passwordpool10[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
            passwordpool2[randint(0, 74)] = inserter  # вставляем
            wordpool4.remove(inserter)  # удаляем из вордпула
            inserter = choice(wordpool4)
            passwordpool3[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool4[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool5[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool6[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool7[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool8[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool9[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
            inserter = choice(wordpool4)
            passwordpool1[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        # Вывод визуала
        # Блок вывода можно будет улучшить
        print(*passwordpool1)
        print(*passwordpool2)
        print(*passwordpool3)
        print(*passwordpool4)
        print(*passwordpool5)
        print(*passwordpool6)
        print(*passwordpool7)
        print(*passwordpool8)
        print(*passwordpool9)
        print(*passwordpool10)
        # Тут я остановился в своем ревью

passwordscreen()  # вызываем экран пароля при запуске
user_try, try_counter = '', 0

# процедура подбора пароля
while True:
    user_try = input()  # повтор ввода
    if user_try == pass_word or user_try == 'skip':
        print('Успешно!')
        break
    try_counter += 1
    if try_counter > 4 and user_try != pass_word:
        print('все возможные попытки исчерпаны')
        print('ТЕРМИНАЛ ЗАБЛОКИРОВАН')
    right_char_counter = 0
    print('Не тот пароль, попробуй снова. Количество попыток ', 5 - try_counter)  # Вывод текста ошибочного пароля
    for i in range(4):
        for j in range(i, 4):
            if user_try[j] == pass_word[i]:
                right_char_counter += 1
    print('Верные символы - ', right_char_counter)


# функциональный блок
def grosstonet(pay):
    ndfl = 0.13
    return pay * (1-ndfl)


def nettogross(pay):
    ndfl = 0.13
    pay = (pay / ((1-ndfl)*100) * 100)
    return int(pay)


def caesar_cipher(lang, k, text):
    result, dict = [], ''
    dictionary_lower, dictionary_upper = '', ''
    if lang == 1:
        dictionary_lower, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
    elif lang == 2:
        dictionary_lower, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLNOPQRSTUVWXYZ"
    for c in range(len(text)):
        if text[c] in dictionary_lower:
            dict = dictionary_lower
        elif text[c] in dictionary_upper:
            dict = dictionary_upper
        else:
            result.append(text[c])
        if text[c] in dict:
            for i in range(len(dict)):
                if 0 <= i + k < len(dict) and text[c] == dict[i]:
                    result.append(dict[i+k])
                elif i + k >= len(dict) and text[c] == dict[i]:
                    result.append(dict[(1 - i - k) % (len(dict) - 1)])
                elif i + k < 0 and text[c] == dict[i]:
                    result.append(dict[(i + k) % len(dict)])
    return ''.join(result)


def caesar_uncipher(lang, k, text):
    result, dict = [], ''
    dictionary_lower, dictionary_upper = '', ''
    if lang == 1:
        dictionary_lower, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
    elif lang == 2:
        dictionary_lower, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLNOPQRSTUVWXYZ"
    for c in range(len(text)):
        if text[c] in dictionary_lower:
            dict = dictionary_lower
        elif text[c] in dictionary_upper:
            dict = dictionary_upper
        else:
            result.append(text[c])
        if text[c] in dict:
            for i in range(len(dict)):
                if 0 <= i - k < len(dict) and text[c] == dict[i]:
                    result.append(dict[i-k])
                elif i - k >= len(dict) and text[c] == dict[i]:
                    result.append()
                elif i - l < 0 and text[c] == dict[i]:
                    result.append(dict[(i-k) % len(dict)])
    return ''.join(result)


def caesar_uncipher2(lang, text):
    result, dict = [], ''
    dictionary_lower, dictionary_upper = '', ''
    if lang == 1:
        dictionary_lower, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
    elif lang == 2:
        dictionary_lower, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLNOPQRSTUVWXYZ"
    for c in range(len(text)):
        if text[c] in dictionary_lower:
            dict = dictionary_lower
        elif text[c] in dictionary_upper:
            dict = dictionary_upper
        else:
            result.append(text[c])



# Блок обработки запросов
while True:
    print('Версия программы 0.03 \n'
          'Доступные команды: \n'
          '1. Рассчитать net-pay из введенного gross-pay \n'
          '2. Рассчитать gross-pay из введенного net-pay \n'
          '3. Шифратор по методу цезаря \n'
          '0. Выход')
    user_try = input()
    if user_try == '1':
        print('Введите gross-pay (только число) \n 0. Назад в главное меню')
        pay = float(input())
        if pay == 0:
            continue
        print(int(grosstonet(pay)))
        continue
    elif user_try == '2':
        print('Введите net-pay (только число) \n'
              '0. Назад в главное меню')
        pay = float(input())
        if pay == 0:
            continue
        print(nettogross(pay))
        continue
    elif user_try == '3':
        user_try = input('1. Зашифровать текст \n'
                         '2. Дешифровать текст \n'
                         '0. Назад в главное меню \n')
        if user_try == '1':
            lang = int(input('Введите язык шифруемого текста \n'
                             '1. Русский \ Russian \n'
                             '2. Английский \ English \n'
                             '0. Назад в главное меню \n'))
            if lang == 0:
                continue
            k = int(input('Введите ключ \n'
                          '0. Назад в главное меню \n'))
            if k == 0:
                continue
            text = input('Введите шифруемый текст \n'
                         '0. Назад в главное меню \n')
            if text == '0':
                continue
            elif lang == 1 or lang == 2:
                print(caesar_cipher(lang, k, text))
                continue
        elif user_try == '2':
            lang = int(input('Введите язык дешифруемого текста \n'
                             '1. Русский \ Russian \n'
                             '2. Английский \ English \n'
                             '0. Назад в главное меню \n'))
            if lang == 0:
                continue
            k = input('Известен ли ключ? \n'
                      '1. Да \n'
                      '2. Нет \n')
            if k == '1':
                k = int(input('Введите ключ \n'
                            '0. Назад в главное меню \n'))
                if k == 0:
                    continue
                text = input('Введите дешифруемый текст \n'
                             '0. Назад в главное меню \n')
                if text == '0':
                    continue
                elif lang == 1 or lang == 2:
                    print(caesar_uncipher(lang, k, text))
                    continue
            elif k == '2':
                print('Секция находится в разработке')
                continue
        elif user_try == '0':
            continue
    elif user_try == '0':
        print('Завершение работы')
        break
    else:
        print('Неизвестная команда. Повторите ввод')
        continue

from random import randint, choice


def passwordscreen():  # функция защитного экрана
    difficulty = 4
    # difficulty = randint(4,6) ## рандомный выбор сложности в разработке
    symbolpool = ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '()']  # 11 символов для визуального шума
    # 76 слов для пароля
    wordpool4 = ['ACID', 'ACHE', 'ALOE', 'BABY', 'BALD', 'BALL', 'CAFE', 'CALL', 'CUNT', 'DARK', 'DEAD', 'DICE', 'EACH',
                 'EARN', 'ECHO', 'FACE', 'FOAM', 'FONT', 'GAIN', 'GANG', 'GOOD', 'HACK', 'HALF', 'HAND', 'IDEA', 'ISLE',
                 'ITEM', 'JAIL', 'JAZZ', 'JUNE', 'KEEP', 'KHAN', 'KISS', 'LADY', 'LAKE', 'LIKE', 'MACE', 'MAIL', 'MASK',
                 'NAVY', 'NAIL', 'NICE', 'OATH', 'OILY', 'ONYX', 'PACE', 'PAIN', 'POOL', 'QAZI', 'QUAD', 'QUBE', 'RACE',
                 'RAIL', 'RARE', 'SACK', 'SAGA', 'SOAP', 'TABU', 'TACT', 'TALC', 'UGLY', 'UNIT', 'URUS', 'VAIN', 'VASE',
                 'VEIN', 'WAGE', 'WAIT', 'WALL', 'XMAS', 'YARD', 'YEAH', 'YOGA', 'ZERO', 'ZETA', 'ZINK']
    # создаем пустые пулы, которые будут выстпупать в роли строк консоли
    passwordpool1, passwordpool2, passwordpool3, passwordpool4, passwordpool5 = [], [], [], [], []
    passwordpool6, passwordpool7, passwordpool8, passwordpool9, passwordpool10 = [], [], [], [], []
    del_wordpool = ['']
    if difficulty == 4:
        while len(passwordpool1) < 75:  # Создаем пять строк с символами визуального шума
            passwordpool1.append(choice(symbolpool))
            passwordpool2.append(choice(symbolpool))
            passwordpool3.append(choice(symbolpool))
            passwordpool4.append(choice(symbolpool))
            passwordpool5.append(choice(symbolpool))
            passwordpool6.append(choice(symbolpool))
            passwordpool7.append(choice(symbolpool))
            passwordpool8.append(choice(symbolpool))
            passwordpool9.append(choice(symbolpool))
            passwordpool10.append(choice(symbolpool))
        # Добавляем слова в строки
        inserter = choice(wordpool4)  # Выбираем фальшивое слово
        passwordpool1[randint(0, 74)] = inserter  # Вставляем
        del_wordpool.append(inserter)  # Сохраняем фальшивое слово в удаленный вордпул
        wordpool4.remove(inserter)  # Удаляем из вордпула
        inserter = choice(wordpool4)
        passwordpool2[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool3[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool4[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool5[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool6[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool7[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool8[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool9[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        inserter = choice(wordpool4)
        passwordpool10[randint(0, 74)] = inserter
        del_wordpool.append(inserter)
        wordpool4.remove(inserter)
        global pass_word
        real_passwordpool = randint(1, 10)  # выбираем строку для иньекции пароля
        pass_word = del_wordpool[real_passwordpool]
        # Вывод визуала
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

    else:
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


def password_generator():
    def is_valid(s):
        if s in yes:
            return 'yeah'
        elif s in no:
            return 'nope'
        else:
            return False

    def generate_password(length, chars):
        password = ''
        for i in range(length):
            password += chars[randint(0, len(chars) - 1)]
        return password

    digits, lowercase_letters = '0123456789', 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation, chars, yes, no = '!#$%&*+-=?@^_', '', ['Да', 'да', 'ДА'], ['Нет', 'нет', 'Нет']
    symb7 = ['i', 'L', 'l', '0', 'o', 'O', '1']
    print('Добро пожаловать в генератор паролей.\n'
          'Количество паролей для генерации?')
    inpt1 = input()
    while True:
        if inpt1.isdigit() is True:
            if int(inpt1) > 0:
                inpt1 = int(inpt1)
                break
            else:
                print('А может быть все-таки введем целое число больше нуля?')
                inpt1 = input()
        else:
            print('А может быть все-таки введем целое число больше нуля?')
            inpt1 = input()
    print('Длина генерируемых паролей?')
    inpt2 = input()
    while True:
        if inpt2.isdigit() is True:
            if int(inpt2) > 0:
                inpt2 = int(inpt2)
                break
            else:
                print('А может быть все-таки введем целое число больше нуля?')
                inpt2 = input()
        else:
            print('А может быть все-таки введем целое число больше нуля?')
            inpt2 = input()
    print('Включать ли цифры?')
    inpt3 = input()
    while is_valid(inpt3) is False:
        print('Не понимаю, попробуй еще раз')
        inpt3 = input()
    if is_valid(inpt3) == 'yeah':
        chars += digits
    print('Включать ли прописные буквы?')
    inpt4 = input()
    while is_valid(inpt4) is False:
        print('Не понимаю, попробуй еще раз')
        inpt4 = input()
    if is_valid(inpt4) == 'yeah':
        chars += uppercase_letters
    print('Включать ли строчные буквы?')
    inpt5 = input()
    while is_valid(inpt5) is False:
        print('Не понимаю, попробуй еще раз')
        inpt5 = input()
    if is_valid(inpt5) == 'yeah':
        chars += lowercase_letters
    print('Включать ли символы?')
    inpt6 = input()
    while is_valid(inpt6) is False:
        print('Не понимаю, попробуй еще раз')
        inpt6 = input()
    if is_valid(inpt6) == 'yeah':
        chars += punctuation
    print('Исключать ли неоднозначные символы il1Lo0O?')
    inpt7 = input()
    while is_valid(inpt7) is False:
        print('Не понимаю, попробуй еще раз')
        inpt7 = input()
    if is_valid(inpt7) == 'yeah':
        for i in range(len(symb7)):
            chars = chars.replace(symb7[i], '')
    print('Ваши пароли:')
    for i in range(inpt1):
        print(generate_password(inpt2, chars))
    print('')


# Блок обработки запросов
while True:
    print('Версия программы 0.05 \n'
          'Доступные команды: \n'
          '1. Рассчитать net-pay из введенного gross-pay \n'
          '2. Рассчитать gross-pay из введенного net-pay \n'
          '3. Генератор безопасного пароля \n'
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
        password_generator()
    elif user_try == '0':
        print('Завершение работы')
        break
    else:
        print('Неизвестная команда. Повторите ввод')
        continue

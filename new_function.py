from random import randint

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


# def caesar_uncipher(lang, k, text):
    # result, dict = [], ''
    # dictionary_lower, dictionary_upper = '', ''
    # if lang == 1:
        # dictionary_lower, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
    # elif lang == 2:
        # dictionary_lower, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLNOPQRSTUVWXYZ"
    # for c in range(len(text)):
        # if text[c] in dictionary_lower:
            # dict = dictionary_lower
        # elif text[c] in dictionary_upper:
            # dict = dictionary_upper
        # else:
            # result.append(text[c])
        # if text[c] in dict:
            # for i in range(len(dict)):
                # if 0 <= i - k < len(dict) and text[c] == dict[i]:
                    # result.append(dict[i-k])
                # elif i - k >= len(dict) and text[c] == dict[i]:
                    # result.append()
                # elif i - l < 0 and text[c] == dict[i]:
                    # result.append(dict[(i-k) % len(dict)])
    # return ''.join(result)


# def caesar_uncipher2(lang, text):
    # result, dict = [], ''
    # dictionary_lower, dictionary_upper = '', ''
    # if lang == 1:
        # dictionary_lower, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
    # elif lang == 2:
        # dictionary_lower, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLNOPQRSTUVWXYZ"
    # for c in range(len(text)):
        # if text[c] in dictionary_lower:
            # dict = dictionary_lower
        # elif text[c] in dictionary_upper:
            # dict = dictionary_upper
        # else:
            # result.append(text[c])


# Блок обработки запросов
while True:
    print('Версия программы - черновая \n'
          'Доступные команды: \n'
          '3. Шифратор по методу цезаря \n'
          '0. Выход')
    user_try = input()
    if user_try == '3':
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
                    # print(caesar_uncipher(lang, k, text))
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

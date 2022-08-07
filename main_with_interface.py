from tkinter import *
from random import randint, choice


def passwordscreen():  # 'Защитный' экран
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
        global pass_word
        pass_word = choice(wordpool4)  # выбираем пароль из пула
        real_passwordpool = randint(1, 10)  # выбираем строку для иньекции пароля
        if real_passwordpool == 1:
            passwordpool1[randint(0, 74)] = pass_word
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
            passwordpool10[randint(0, 74)] = inserter
            wordpool4.remove(inserter)
        elif real_passwordpool == 2:
            passwordpool2[randint(0, 74)] = pass_word
            wordpool4.remove(pass_word)
            inserter = choice(wordpool4)  # выбираем фальшивое слово
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
        lbl1 = Label(window, text = passwordpool1, font = ("Arial Bold", 10))
        lbl1.grid(column = 0, row = 0)
        lbl2 = Label(window, text = passwordpool2, font = ("Arial Bold", 10))
        lbl2.grid(column = 0, row = 1)
        lbl3 = Label(window, text = passwordpool3, font = ("Arial Bold", 10))
        lbl3.grid(column = 0, row = 2)
        lbl4 = Label(window, text = passwordpool4, font = ("Arial Bold", 10))
        lbl4.grid(column = 0, row = 3)
        lbl5 = Label(window, text = passwordpool5, font = ("Arial Bold", 10))
        lbl5.grid(column = 0, row = 4)
        lbl6 = Label(window, text = passwordpool6, font = ("Arial Bold", 10))
        lbl6.grid(column = 0, row = 5)
        lbl7 = Label(window, text = passwordpool7, font = ("Arial Bold", 10))
        lbl7.grid(column = 0, row = 6)
        lbl8 = Label(window, text = passwordpool8, font = ("Arial Bold", 10))
        lbl8.grid(column = 0, row = 7)
        lbl9 = Label(window, text = passwordpool9, font = ("Arial Bold", 10))
        lbl9.grid(column = 0, row = 8)
        lbl10 = Label(window, text = passwordpool10, font = ("Arial Bold", 10))
        lbl10.grid(column = 0, row = 9)

window = Tk()
window.title('pythonProject')
window.geometry('1000x500')
passwordscreen()
window.mainloop()


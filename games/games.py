
import easygui
import random
title = "game"


def rock_paper_scissors():
    easygui.msgbox('Здесь будет игра "Камень, ножницы, бумага"')
    images = ['rock.png', 'scissors.png', 'paper.png']
    a = {
        0: 1,
        1: 2,
        2: 0
    }

    num = random.randrange(0, 3)
    choice = easygui.buttonbox(
        "Что выбирете?", "Камень, ножницы, бумага", images=images, choices=[])
    if choice:
        choice = images.index(choice)
    else:
        return None
    if a[choice] == num:
        easygui.buttonbox("Ты победил(а)!", "Камень, ножницы, бумага", images=[
            images[choice], "gt.png", images[num]], choices=["Вернуться в меню"])
    elif a[num] == choice:
        easygui.buttonbox("Ты проиграл(а)!", "Камень, ножницы, бумага", images=[
            images[choice], "lt.png", images[num]], choices=["Вернуться в меню"])
    else:
        easygui.buttonbox("Ничья!", "Камень, ножницы, бумага", images=[
            images[choice], "eq.png", images[num]], choices=["Вернуться в меню"])


num = random.randrange(1, 10)


def guess_the_number():
    easygui.msgbox('Здесь будет игра "Угадай число"')
    out = easygui.integerbox(
        "Введите число которое загадал комп  от 1 до 10", title)
    if out < num:
        easygui.msgbox("Нет число больше")
    elif out > num:
        easygui.msgbox("Нет число больше")
    else:
        easygui.msgbox("Угадал(а)")
    easygui.msgbox(num)


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()

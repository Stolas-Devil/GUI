
import easygui
import random
title = "game"


def rock_paper_scissors():
    easygui.msgbox('Здесь будет игра "Камень, ножницы, бумага"')


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

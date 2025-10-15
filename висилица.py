import os


# Очистка консоли
clear = lambda: os.system('cls')


print("Привет! Я загадал слово, твоя задача - угадать его по буквам. ")
input("Нажми Enter, когда будешь готов(а) начать игру. ")
clear()
print("Поехали!")

word = "пайтон" #слово для угадывания

list = []

hp = 10 

while hp > 0:
    letter = input("Введи букву: ").lower()

    list.append(letter) # Добавить букву в список

    if letter not in word:
        hp -= 1
    print("У тебя осталось", hp, "жизней.")

    opened =""
    for i in word:
        if i in list:
            opened += i
        else:
            opened += "*"

    print("слово:", opened)

    #проверка победы 
    if opened == word:
        print("Поздравляю! Ты угадал(а) слово!", word)
        break #остановить цикл
import random

words = ["cat", "dog", "sun"]

word = random.choice(words)

guess = ""
chance = 5

print("🎮 Hangman Game")

while chance > 0:

    show = ""

    for i in word:
        if i in guess:
            show += i + " "
        else:
            show += "_ "

    print(show)

    if "_" not in show:
        print("🎉 You Win")
        break

    letter = input("Enter letter: ")

    guess += letter

    if letter not in word:
        chance -= 1
        print("❌ Wrong")
        print("Chances left:", chance)

if chance == 0:
    print("💀 Game Over")
    print("Word was:", word)

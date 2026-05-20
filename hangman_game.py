import random

# Predefined words
word_list = ["python", "banana", "school", "planet", "guitar"]

# Randomly choose a word
secret_word = random.choice(word_list)

guessed_letters = []
attempts_left = 6

print("🎮 Welcome to Hangman Game")
print("Guess the word one letter at a time!")

while attempts_left > 0:

    # Display hidden word
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("🎉 You Won!")
        print("The word was:", secret_word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("⚠ Letter already guessed.")
        continue

    guessed_letters.append(guess)

    # Correct or wrong guess
    if guess in secret_word:
        print("✅ Correct!")
    else:
        attempts_left -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts_left)

# If player loses
if attempts_left == 0:
    print("\n💀 Game Over!")
    print("Correct word was:", secret_word)

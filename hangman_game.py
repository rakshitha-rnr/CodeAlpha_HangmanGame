import random

# List of words
words = ["python", "laptop", "guitar", "college", "student"]

# Choose random word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman Game")
print("Guess the word letter by letter!")

# Game loop
while wrong_guesses < max_guesses:

    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win
    if "_" not in display_word:
        print("🎉 Congratulations! You Won!")
        print("The word was:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1:
        print("⚠ Enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_guesses - wrong_guesses)

# Lose condition
if wrong_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("Correct word was:", word)

print("\nThanks for playing Hangman Game 🎮")

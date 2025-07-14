import random

Hangman_words = [
    "python", "hangman", "developer", "function", "program",
    "variable", "computer", "keyboard", "iteration", "condition"
]

Max_attempts=6

def choose_word():
    return random.choice(Hangman_words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    word = choose_word()
    guessed_letters = set()
    wrong_attempts = 0

    print("Welcome to the Hangman Game!")
    print(f"The word has {len(word)} letters. You have {Max_attempts} incorrect attempts.")
    print(display_word(word, guessed_letters))

    while wrong_attempts < Max_attempts:
        try:
            guess = input("\nGuess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Please enter a single alphabetic character.")
            if guess in guessed_letters:
                raise ValueError("You already guessed that letter. Try a different one.")

            guessed_letters.add(guess)

            if guess in word:
                print("Good job! That letter is in the word.")
            else:
                wrong_attempts += 1
                print(f"Wrong guess! Attempts remaining: {Max_attempts - wrong_attempts}")

            print(display_word(word, guessed_letters))

            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word correctly and won the game!")
                return

        except ValueError as ve:
            print(f"Error: {ve}")


    print(f"\nYou lost! The word was: '{word}'. The monster ate you!")

if __name__ == "__main__":
    hangman_game()            
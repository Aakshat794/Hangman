import random

def display_intro():
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You can make a limited number of incorrect guesses.")
    print("Good luck!\n")

def choose_word():
    words = ["python", "hangman", "developer", "programming", "challenge"]
    return random.choice(words)

def display_word_progress(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    display_intro()
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6
    
    while attempts_left > 0:
        print("Word to guess: ", display_word_progress(word_to_guess, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Good job! That letter is in the word.\n")
            if all(letter in guessed_letters for letter in word_to_guess):
                print("Congratulations! You guessed the word correctly: ", word_to_guess)
                return
        else:
            attempts_left -= 1
            print("Oops! That letter is not in the word.\n")
    
    print("Game over! The correct word was:", word_to_guess)
    
if __name__ == "__main__":
    hangman()

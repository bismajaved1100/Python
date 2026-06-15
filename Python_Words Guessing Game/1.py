import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

def get_secret(level):
    if level == "easy":
        return random.choice(easy_words)
    elif level == "medium":
        return random.choice(medium_words)
    elif level == "hard":
        return random.choice(hard_words)
    else:
        print("Invalid choice. Defaulting to easy level.")
        return random.choice(easy_words)

print("--- Welcome to the Words Guessing Game ---")
level = input('Choose difficulty (easy, medium, hard): ').lower()
secret = get_secret(level)
attempts = 0

while True:
    guess = input("\nEnter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        n = int(input("Play again? 1. Yes  2. No: "))
        if n == 1:
            level = input('Choose difficulty: ').lower()
            secret = get_secret(level)
            attempts = 0
            continue
        else:
            break

    # 4. Advanced Hint System
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        elif i < len(guess) and guess[i] in secret:
            hint += "?"
        else:
            hint += "-"
    
    print("Hint: " + hint + "  (-: missing, ?: wrong spot)")

print("Game Over. Thanks for playing!")
import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium or hard")

level = input('Enter difficulty: '). lower()
if level == "easy":
    secret = random. choice(easy_words)
elif level == "medium":
    secret = random. choice(medium_words)
elif level == "hard":
    secret = random. choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random. choice(easy_words)

attempts = 0
print("\nGuess the secret password!")

# 3. Game loop
while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        n = int(input("Try Again? 1.yes  2.no"))
        if(n == 1):
            break
        else:
            level = input('Enter difficulty: '). lower()
            if level == "easy":
                secret = random. choice(easy_words)
            elif level == "medium":
                secret = random. choice(medium_words)
            elif level == "hard":
                secret = random. choice(hard_words)
            else:
                print("Invalid choice. Defaulting to easy level")
                secret = random. choice(easy_words)

            attempts = 0
            continue

    # 4. Give a hint: show which letters are correct (like Wordle)
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "-"
    print("Hint: " + hint)

print("Game Over.")
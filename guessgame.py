import random

name = input("Enter your name: ")
rand_num = random.randint(1, 50)
guesses_left = 5
won = False

while guesses_left > 0: 
    try:
        guess = int(input(f"Enter your guess {5 - guesses_left + 1} (1-50): "))
        if guess == rand_num:
            print("You win!")
            won = True
            break
        elif guess < rand_num:
            print("Too low!")
        else:
            print("Too high!")
        guesses_left -= 1  # Only decrease on valid guess
    except ValueError:
        print("Please enter a valid number!")  # Invalid doesn’t count

with open("winners.txt", "w") as file:  # Plural "winners.txt"
    if won:
        file.write(f"Winner: {name}")
    else:
        file.write(f"Loser: {name}")
        print(f"Game Over! The number was {rand_num}")

with open("winners.txt", "r") as file:
    content = file.read()
    print(content)

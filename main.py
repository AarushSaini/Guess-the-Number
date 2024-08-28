import random

def generate_random_number(start=1, end=100):
    return random.randint(start, end)

def get_user_guess():
    return int(input("Enter your guess: "))

def check_guess(user_guess, rand_number):
    if user_guess == rand_number:
        return "correct"
    elif user_guess > rand_number:
        return "high"
    else:
        return "low"

def main():
    rand_number = generate_random_number()
    user_guess = None
    guesses = 0

    while user_guess != rand_number:
        user_guess = get_user_guess()
        guesses += 1
        result = check_guess(user_guess, rand_number)

        if result == "correct":
            print("You guessed it right!")
        elif result == "high":
            print("You guessed it wrong! Enter a smaller number.")
        else:
            print("You guessed it wrong! Enter a larger number.")

    print(f"You guessed the number in {guesses} guesses.")

if __name__ == "__main__":
    main()

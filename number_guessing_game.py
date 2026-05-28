

import random

def display_welcome():
    print("=" * 40)
    print("       WELCOME TO GUESS THE NUMBER!    ")
    print("=" * 40)

def choose_difficulty():
    print("\nChoose Difficulty:")
    print("  1. Easy   → 10 chances (1–50)")
    print("  2. Medium → 7 chances  (1–100)")
    print("  3. Hard   → 5 chances  (1–200)")
    print("-" * 40)

    choice = input("Enter 1, 2 or 3: ").strip()

    if choice == "1":
        return 50, 10, "Easy"
    elif choice == "2":
        return 100, 7, "Medium"
    elif choice == "3":
        return 200, 5, "Hard"
    else:
        print("Invalid choice. Setting to Medium by default.")
        return 100, 7, "Medium"

def get_guess(max_number):
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_number}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def give_hint(guess, secret):
    difference = abs(secret - guess)

    if difference == 0:
        return None
    elif difference <= 5:
        return "🔥 Extremely Hot! So close!"
    elif difference <= 15:
        return "♨️  Very Warm! Getting there!"
    elif difference <= 30:
        return "😐 Lukewarm. Keep trying."
    elif difference <= 50:
        return "🧊 Cold. Think bigger or smaller."
    else:
        return "❄️  Ice Cold! Way off!"

def play_game():
    display_welcome()

    max_number, max_attempts, difficulty = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts_used = 0

    print(f"\n🎯 Guess the number between 1 and {max_number}")
    print(f"🎮 Difficulty: {difficulty} | Chances: {max_attempts}\n")
    print("-" * 40)

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        print(f"Attempts remaining: {remaining}")

        guess = get_guess(max_number)
        attempts_used += 1

        if guess == secret_number:
            print("\n" + "=" * 40)
            print(f"  🎉 CORRECT! The number was {secret_number}!")
            print(f"  ✅ You got it in {attempts_used} attempt(s)!")

            if attempts_used == 1:
                print("  🏆 LEGENDARY! First try!")
            elif attempts_used <= max_attempts // 2:
                print("  ⭐ Excellent performance!")
            else:
                print("  👍 Well done!")

            print("=" * 40)
            return True

        elif guess < secret_number:
            print("📈 Too Low!")
        else:
            print("📉 Too High!")

        hint = give_hint(guess, secret_number)
        if hint:
            print(hint)

        print("-" * 40)

    print("\n" + "=" * 40)
    print(f"  💀 GAME OVER! You ran out of chances.")
    print(f"  🔢 The number was: {secret_number}")
    print("=" * 40)
    return False

def main():
    while True:
        play_game()

        print("\nWould you like to play again?")
        replay = input("Enter 'yes' to play again or 'no' to quit: ").strip().lower()

        if replay in ["yes", "y"]:
            print("\n🔄 Starting a new game...\n")
        else:
            print("\n👋 Thanks for playing! See you next time.")
            print("    github.com/asvincrypto")
            print("=" * 40)
            break

if __name__ == "__main__":
    main()

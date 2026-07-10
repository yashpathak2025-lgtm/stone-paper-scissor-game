import random

choices = ["stone", "paper", "scissor"]


def winner(user, computer):
    if user == computer:
        return "draw"

    if (
        (user == "stone" and computer == "scissor")
        or (user == "paper" and computer == "stone")
        or (user == "scissor" and computer == "paper")
    ):
        return "user"

    return "computer"


player_score = 0
computer_score = 0
draws = 0

print("=" * 25, "STONE PAPER SCISSOR GAME", "=" * 25)

while True:

    user = input("\nEnter Stone, Paper, or Scissor: ").lower().strip()

    if user not in choices:
        print("❌ Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose      : {user}")
    print(f"Computer chose : {computer}")

    result = winner(user, computer)

    if result == "draw":
        print("🤝 It's a Draw!")
        draws += 1

    elif result == "user":
        print("🎉 You Win!")
        player_score += 1

    else:
        print("💻 Computer Wins!😡😠")
        computer_score += 1

    print("\n------ Score Board ------")
    print(f"You      : {player_score}")
    print(f"Computer : {computer_score}")
    print(f"Draws    : {draws}")
    print("-------------------------")

    play = input("\nPlay Again? (yes/no): ").lower().strip()

    if play != "yes":
        print("\n========== Final Score ==========")
        print(f"You      : {player_score}")
        print(f"Computer : {computer_score}")
        print(f"Draws    : {draws}")

        if player_score > computer_score:
            print("\n🏆 Congratulations! You won the game.")
        elif computer_score > player_score:
            print("\n💻 Computer won the game.")
        else:
            print("\n🤝 Overall Match Draw.")

        print("\nThanks for playing! ❤️")
        break
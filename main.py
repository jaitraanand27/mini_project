from quiz_questions import start_quiz, show_instructions


def main():
    while True:
        print("\n===== QUIZ APPLICATION =====")
        print("1. Start Quiz")
        print("2. View Quiz Instructions")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                start_quiz()

                replay = input(
                    "\nWould you like to play again? (yes/no): "
                ).lower()

                if replay == "yes":
                    print("\nStarting a new quiz...")
                    continue
                elif replay == "no":
                    print("Thank you for playing!")
                    return
                else:
                    print("Invalid choice! Please enter yes or no.")

        elif choice == "2":
            show_instructions()

        elif choice == "3":
            print("Thank you for using the Quiz Application!")
            break

        else:
            print("Invalid menu choice! Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
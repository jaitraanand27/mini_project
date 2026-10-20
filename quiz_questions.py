from questions import questions


def show_instructions():
    print("\n===== QUIZ INSTRUCTIONS =====")
    print("1. The quiz contains 5 questions.")
    print("2. Each question has four options: A, B, C, D.")
    print("3. Enter one option for each question.")
    print("4. Each correct answer gets 1 point.")
    print("5. Wrong answers get 0 points.")
    print("6. Your final score and percentage will be displayed.")


def start_quiz():
    correct = 0
    incorrect = 0

    print("\n===== WELCOME TO PYTHON QUIZ =====")
    print("Answer the following questions.\n")

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for option, value in q["options"].items():
            print(f"{option}. {value}")

        while True:
            answer = input("Enter your answer: ").upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice! Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct answer!")
            correct += 1
        else:
            print("Incorrect answer!")
            print("Correct answer:", q["answer"])
            incorrect += 1

    total = len(questions)
    percentage = (correct / total) * 100

    print("\n===== QUIZ RESULTS =====")
    print("Total Questions:", total)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Final Score:", correct, "/", total)
    print("Final Percentage:", percentage, "%")

    if percentage == 100:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good job!")
    else:
        print("Performance: Keep practicing!")
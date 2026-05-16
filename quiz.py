from functools import reduce

# -------------------------------
# Quiz Data: Nested List
# [question, [options], correct_option_letter]
# -------------------------------
quiz_questions = [
    [
        "What is the capital of India?",
        ["a) New Delhi", "b) Mumbai", "c) Chennai", "d) Kolkata"],
        "a"
    ],
    [
        "Which data type is used to store text in Python?",
        ["a) int", "b) str", "c) float", "d) bool"],
        "b"
    ],
    [
        "Which symbol is used for comments in Python?",
        ["a) //", "b) <!-- -->", "c) #", "d) /* */"],
        "c"
    ],
    [
        "What does CPU stand for?",
        ["a) Central Processing Unit", "b) Computer Personal Unit",
         "c) Central Print Unit", "d) Control Panel Unit"],
        "a"
    ],
    [
        "Which keyword is used to define a function in Python?",
        ["a) func", "b) define", "c) def", "d) function"],
        "c"
    ]
]

# This list will track all scores to find the highest score
all_scores = []


# -------------------------------
# Function to ask questions
# -------------------------------
def ask_questions(questions):
    user_answers = []
    correct_answers = []

    print("\n--- QUIZ STARTS ---\n")

    # Loop through each question
    for index, q in enumerate(questions, start=1):
        question_text = q[0]
        options = q[1]
        correct = q[2]

        print(f"Q{index}. {question_text}")
        for option in options:
            print(option)

        # Accept answer and use string methods
        answer = input("Your answer (a/b/c/d): ")
        answer = answer.strip().lower()   # string methods for comparison

        user_answers.append(answer)
        correct_answers.append(correct)

        print()  # blank line for neatness

    return user_answers, correct_answers


# -------------------------------
# Function to calculate score
# Uses map to compare answers
# Uses reduce to sum scores
# -------------------------------
def calculate_score(user_answers, correct_answers, questions):
    # map to evaluate answers: 1 for correct, 0 for incorrect
    result_list = list(
        map(lambda pair: 1 if pair[0] == pair[1] else 0,
            zip(user_answers, correct_answers))
    )

    # reduce to compute total score
    total_score = reduce(lambda x, y: x + y, result_list, 0)

    # Question-by-question result
    print("\n--- QUESTION-BY-QUESTION RESULT ---")
    for i, (ua, ca, res) in enumerate(zip(user_answers, correct_answers, result_list), start=1):
        status = "Correct" if res == 1 else "Incorrect"
        print(f"Q{i}: Your answer = {ua}, Correct answer = {ca} -> {status}")

    # Total score and percentage
    num_questions = len(questions)
    percentage = (total_score / num_questions) * 100

    print("\n--- FINAL RESULT ---")
    print(f"Total Score: {total_score} / {num_questions}")
    print(f"Percentage: {percentage:.2f}%")

    # Pass / Fail (you can change pass percentage)
    if percentage >= 50:
        print("Result: PASS ✅")
    else:
        print("Result: FAIL ❌")

    return total_score, percentage


# -------------------------------
# Recursive function to play quiz again
# -------------------------------
def play_quiz():
    # Ask questions
    user_answers, correct_answers = ask_questions(quiz_questions)

    # Calculate score
    score, percentage = calculate_score(user_answers, correct_answers, quiz_questions)

    # Track scores in list and show highest score
    all_scores.append(score)
    highest_score = max(all_scores)

    print(f"\nHighest score achieved so far: {highest_score} / {len(quiz_questions)}")

    # Ask user if they want to replay (recursion)
    choice = input("\nDo you want to play again? (yes/no): ")
    choice = choice.strip().lower()

    if choice == "yes":
        print("\nRestarting the quiz...\n")
        play_quiz()   # recursion
    else:
        print("\nThank you for playing the quiz! 😊")


# -------------------------------
# Main entry point
# -------------------------------
if __name__ == "__main__":
    play_quiz()

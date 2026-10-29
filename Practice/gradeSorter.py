import random

def make_question(grade): 
    """Return (question_text, correct_answer) for the grade level."""
    if grade == 1:
        a, b = random.randint(1, 100), random.randint(1, 100)
        return f"{a} + {b}", a + b
    elif grade == 2:
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} x {b}", a * b
    else:
        divisor = random.randint(1, 10)
        answer = random.randint(1, 10)
        return f"{divisor * answer} / {divisor}", answer

def get_int(prompt, low=None, high=None):
    while True:
        try:
            value = int(input(prompt))
            if (low is None or value >= low) and (high is None or value <= high):
                return value
        except ValueError:
            pass
        print("Please enter a valid number.")

def letter_grade(score):
    return {4: "A", 3: "B", 2: "C", 1: "D", 0: "F"}[score] #establish grade score range to letter grades

FILENAME = "quizScore.txt"
NUM_STUDENTS = 5 # the number of test takers; change this if you want to test more or less students 

open(FILENAME, "w").close()  # we need to start with a clean file

for student in range(NUM_STUDENTS):
    print(f"\nStudent {student + 1} of {NUM_STUDENTS}")
    name = input("Please enter your name: ")
    grade = get_int("Enter your grade level (1-3): ", 1, 3)

    score = 0 # initialize score
    missed = []
    for q in range(1, 5):
        text, answer = make_question(grade)
        guess = get_int(f"Question {q}: {text} = ")
        if guess == answer:
            score += 1
            print("Correct, great job!")
        else:
            print("Incorrect.")
            missed.append((text, answer))

    print(f"You scored {score}/4.")
    if missed:  # personal aditional is the option to review missed questions help the children learn
        print("Review:")
        for text, answer in missed:
            print(f"  {text} = {answer}")

    with open(FILENAME, "a") as f:
        f.write(f"{name}|{grade}|{score}\n")

# Read the file and print results
print("\nQuiz Results")
scores = []
with open(FILENAME, "r") as f:
    for line in f:
        name, grade, score = line.strip().split("|")
        score = int(score)
        scores.append((name, score))
        print(f"Name: {name} | Grade Level: {grade} | Score: {score} | Grade: {letter_grade(score)}")

# An extra element this displays the class total stats
average = sum(s for _, s in scores) / len(scores)
top_name, top_score = max(scores, key=lambda x: x[1])
print(f"\nClass average: {average:.2f}/4")
print(f"Congratulations!\nTop scorer: {top_name} ({top_score}/4)!!")

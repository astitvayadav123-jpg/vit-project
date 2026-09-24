import random

questions = [
    ["""What is the capital of India?
    a)delhi
    b)punjab
    c)gujrat
    d)lahore""", "a"],
    ["""What is 2 + 2?
    a)4
    b)5
    c)6
    d)7""", "a"],
    ["""Which language are we using?
    a)java
    b)python
    c)c#
    d)c#.net""", "b"],
    ["""What is 5*5?
    a)30
    b)40
    c)25
    d)60""","c"],
    ["""How many days are there in a week?
    a)5
    b)6
    c)7
    d)8
    """, "c"]
]

# Randomize questions
random.shuffle(questions)

correct = 0
incorrect = 0
total_questions = 0

print("QUIZ")
print("The quiz will end after 3 incorrect answers.\n")

for question in questions:

    # Stop if 3 answers are incorrect
    if incorrect == 3:
        break

    print(question[0])

    answer = input("Your answer: ")

    total_questions += 1

    if answer.lower() == question[1].lower():
        print("Correct!\n")
        correct += 1
    else:
        print("Incorrect!")
        print("Correct answer:", question[1])
        print()
        incorrect += 1


print("QUIZ RESULT")
print("Total questions attempted:", total_questions)
print("Correct answers:", correct)
print("Incorrect answers:", incorrect)
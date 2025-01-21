import random

def generate_equation():
    """To generate a random a(+-*/)b=x equation"""
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    a = random.randint(1,1000)
    x = random.randint(1,1000)
    
    if operator == '+':
        b = a + x
    elif operator == '-':
        b = a - x
    elif operator == '*':
        b = a * x
    elif operator == '/':
        # Ensures number is divisible into a whole integer
        b = a * x
        a = b

    return a, x, b, operator

def ask_question(a, b, operator):
    """To ask user to solve equation"""
    print(f"Solve: {a} {operator} x = {b}")
    while True:
        try:
            user_answer = int(input("What is x?"))
            return user_answer
        except ValueError:
            print("Answer is invalid, please enter an integer value")

def check_answer(user_answer, correct_answer):
    """To check is users answer is correct/incorrect and output respective result"""
    return user_answer == correct_answer

def main():
    """This function runs the math game"""
    print("Welcome to the Game of Maths")
    print("Solve the equation correctly and earn points!")

    num_questions = 10
    score = 0

    for i in range(num_questions):
        print(f"Question {i +1}:")
        a, x, b, operator = generate_equation()
        user_answer = ask_question(a ,b, operator)

        if check_answer(user_answer, x):
            print("Well done, you've gained a point!")
            score += 1
        else:
            print(f"Incorrect, the correct answer was {x}.\n")

    print(f"Game Over! Your score was {score}/{num_questions}.")

if __name__ == "__main__":
    main()



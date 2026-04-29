import random

def show_instructions():
    print("=== 100以内加减法练习题 ===")
    print("包含加法、减法，每行5个算式，答案请写在横线上。\n")

def generate_question_with_answer():
    if random.choice([True, False]):
        a = random.randint(0, 100)
        b = random.randint(0, 100 - a)
        answer = a + b
        question_str = f"{a} + {b} = ______"
        return question_str, answer
    else:
        a = random.randint(0, 100)
        b = random.randint(0, a)
        answer = a - b
        question_str = f"{a} - {b} = ______"
        return question_str, answer


def print_questions(questions):
    print("\n=== 练习题 ===")
    for idx, q in enumerate(questions, 1):
        print(f"{idx:2d}.{q:<15}", end="  ")
        if idx % 5 == 0:
            print()
    if len(questions) % 5 != 0:
        print()


def print_answers(answers):
    print("\n=== 参考答案===")
    for idx, ans in enumerate(answers, 1):
        print(f"{idx:2d}.{ans:^6}", end="    ")
        if idx % 5 == 0:
            print()
    if len(answers) % 5 != 0:
        print()


# 主程序
def main():
    show_instructions()

    questions = []
    answers = []
    for _ in range(50):
        q, a = generate_question_with_answer()
        questions.append(q) #生成问题后保留
        answers.append(a)   #同时保留答案

    print_questions(questions)

    print_answers(answers)


if __name__ == "__main__":
    main()
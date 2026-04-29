import random

def gen_addition(max_num=100):
    a = random.randint(0, max_num)
    b = random.randint(0, max_num - a)
    return f"{a}+{b}", a + b

def gen_subtraction(max_num=100):
    a = random.randint(0, max_num)
    b = random.randint(0, a)
    return f"{a}-{b}", a - b

def gen_mixed(max_num=100):
    if random.choice([True, False]):
        return gen_addition(max_num)
    else:
        return gen_subtraction(max_num)


def generate_question_set(generator_func, count=50, max_num=100):
    questions = []  # 存储算式字符串（带填空）
    answers = []  # 存储答案
    for _ in range(count):
        expr, ans = generator_func(max_num)
        # 将表达式转换为显示格式（带填空）
        display_expr = expr.replace("+", " + ").replace("-", " - ")
        questions.append(f"{display_expr} = ______")
        answers.append(ans)
    return questions, answers


def print_questions(questions, title="练习题"):
    print(f"\n=== {title} ===")
    for idx, q in enumerate(questions, 1):
        print(f"{idx:2d}.{q:<18}", end="  ")
        if idx % 5 == 0:
            print()
    if len(questions) % 5 != 0:
        print()


def print_answers(answers, title="参考答案"):
    print(f"\n=== {title} ===")
    for idx, ans in enumerate(answers, 1):
        print(f"{idx:2d}.{ans:^6}", end="    ")
        if idx % 5 == 0:
            print()
    if len(answers) % 5 != 0:
        print()


def show_instructions():
    print("=== 100以内加减法练习题（算式与算法分离）===")
    print("支持：全加法 / 全减法 / 混合算式\n")


if __name__ == "__main__":
    show_instructions()

    # 1. 全加法
    q1, a1 = generate_question_set(gen_addition, 50, 100)
    print_questions(q1, "全加法算式习题")
    print_answers(a1, "全加法参考答案")

    # 2. 全减法
    q2, a2 = generate_question_set(gen_subtraction, 50, 100)
    print_questions(q2, "全减法算式习题")
    print_answers(a2, "全减法参考答案")

    # 3. 混合算式
    q3, a3 = generate_question_set(gen_mixed, 50, 100)
    print_questions(q3, "混合算式习题")
    print_answers(a3, "混合算式参考答案")
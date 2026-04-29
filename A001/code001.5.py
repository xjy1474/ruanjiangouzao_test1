import random


def gen_addition(max_num):
    a = random.randint(0, max_num)
    b = random.randint(0, max_num - a)
    return f"{a}+{b}", a + b


def gen_subtraction(max_num):
    a = random.randint(0, max_num)
    b = random.randint(0, a)
    return f"{a}-{b}", a - b


def gen_mixed(max_num):
    if random.choice([True, False]):
        return gen_addition(max_num)
    else:
        return gen_subtraction(max_num)

def generate_unique_question_set(generator_func, max_num, count=50):
    questions = []
    answers = []
    seen = set()

    while len(questions) < count:
        expr, ans = generator_func(max_num)
        if expr not in seen:
            seen.add(expr)
            display_expr = expr.replace("+", " + ").replace("-", " - ")
            questions.append(f"{display_expr} = ______")
            answers.append(ans)

    return questions, answers


def print_questions(questions, title="无重复练习题"):
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


def show_instructions(max_num):
    print(f"=== {max_num}以内加减法练习题 ===")
    print("支持混合加减法，自动检查并避免重复算式\n")


if __name__ == "__main__":
    max_num = int(input("请输入限制条件："))

    show_instructions(max_num)

    questions, answers = generate_unique_question_set(gen_mixed, max_num, 50)

    print_questions(questions, f"{max_num}以内无重复混合算式")
    print_answers(answers, "参考答案")
import random
#随机生成50道100以内加减法运算
print("=== 50道100以内加减法口算题 ===\n")

for i in range(1, 51):
    if random.choice([True, False]):
        a = random.randint(0, 100)
        b = random.randint(0, 100 - a)
        print(f"{i:2d}. {a} + {b} = ______")
    else:
        a = random.randint(0, 100)
        b = random.randint(0, a)
        print(f"{i:2d}. {a} - {b} = ______")
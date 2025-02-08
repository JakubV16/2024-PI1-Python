import random

def generate_example():
    while True:
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 25)
        operation = random.choice(["+", "-"])

        if operation == "+" and 1 <= num1 + num2 <= 25:
            return f"{num1} + {num2} = ?"
        elif operation == "-" and 1 <= num1 - num2 <= 25:
            return f"{num1} - {num2} = ?"

# Generovanie 5 náhodných príkladov
for _ in range(5):
    print(generate_example())
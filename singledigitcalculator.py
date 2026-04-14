def first_digit():
    return int(input("Type your first digit: "))


def symbol():
    return input("Which symbol do you want to use? (+, -, *, /): ")


def second_digit():
    return int(input("Type your second digit: "))


Fdigit = first_digit()
sym = symbol()
Sdigit = second_digit()


if sym == "+":
    answer = Fdigit + Sdigit
elif sym == "-":
    answer = Fdigit - Sdigit
elif sym == "*":
    answer = Fdigit * Sdigit
elif sym == "/":
    answer = Fdigit / Sdigit
else:
    answer = "Invalid symbol"


print(f"Your answer is {answer}")

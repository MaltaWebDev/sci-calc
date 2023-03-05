import math

while True:
    print("\nChoose the mathematical operation:\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raise to nth power\n6 - Logarithm\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    oper = input("\nYour option from the menu: ")

    if oper == "0":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one + value_two}")
        break


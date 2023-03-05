import math


while True:
    print("\n=======================================================\n                      Sci-calc\n=======================================================\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raise to nth power\n6 - Logarithm\n7 - Sine\n8 - Cosine\n9 - Tangent\n=======================================================")

    oper = input("\nChoose an option from the menu: ")

    # addition
    if oper == "0":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one + value_two}")
        break

    # subtration
    elif oper == "1":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one - value_two}")
        break

    # multiplication
    elif oper == "2":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one * value_two}")
        break

    # division
    elif oper == "3":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one / value_two}")
        break

    # modulo
    elif oper == "4":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one % value_two}")
        break
        
    # raise to nth power
    elif oper == "5":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nPower to raise to:"))
        print(f"The answer is: {value_one ** value_two}")
        break

    elif oper == "6":
        # value_one = float(input("\nFirst value:"))
        # value_two = float(input("\nSecond value:"))
        # print(f"The answer is: {value_one / value_two}")
        print("coming soon...")
        break

    elif oper == "7":
        # value_one = float(input("\nFirst value:"))
        # value_two = float(input("\nSecond value:"))
        # print(f"The answer is: {value_one / value_two}")
        print("coming soon...")
        break

    elif oper == "8":
        # value_one = float(input("\nFirst value:"))
        # value_two = float(input("\nSecond value:"))
        # print(f"The answer is: {value_one / value_two}")
        print("coming soon...")
        break

    elif oper == "9":
        # value_one = float(input("\nFirst value:"))
        # value_two = float(input("\nSecond value:"))
        # print(f"The answer is: {value_one / value_two}")
        print("coming soon...")
        break

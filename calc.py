import math


while True:
    print("\n=======================================================\n                      Sci-Calc\n=======================================================\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raise to nth power\n6 - Logarithm\n7 - Sine\n8 - Cosine\n9 - Tangent\n=======================================================")

    oper = input("\nChoose an option from the menu: ")

    # Addition
    if oper == "0": 
        value_one = float(input("\nFirst value: "))
        value_two = float(input("\nSecond value: "))
        print(f"\nThe answer is: {value_one + value_two}")
        go_back = input("\nGo back to the main menu? (Y/N): ")
        
        if go_back.upper() == "Y":
            continue
        else:
            break

    # Subtration
    elif oper == "1":
        value_one = float(input("\nFirst value: "))
        value_two = float(input("\nSecond value: "))
        print(f"The answer is: {value_one - value_two}")
        break

    # Multiplication
    elif oper == "2":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one * value_two}")
        break

    # Division
    elif oper == "3":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one / value_two}")
        break

    # Modulo
    elif oper == "4":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nSecond value:"))
        print(f"The answer is: {value_one % value_two}")
        break
        
    # Raise to nth power
    elif oper == "5":
        value_one = float(input("\nFirst value:"))
        value_two = float(input("\nPower to raise to:"))
        print(f"The answer is: {value_one ** value_two}")
        break

    # Logarithm
    elif oper == "6":
        value_one = float(input("\nEnter value: "))
        base = float(input("\nBase of the logarith :"))
        print(f"The answer is: {math.log(value_one, base)}")
        break
    
    # Sine
    elif oper == "7":
        value_one = float(input("\nEnter the angle in radians: "))
        print(f"The answer is: {math.sin(value_one)}")
        break

    # Cosine
    elif oper == "8":
        value_one = float(input("\nEnter the angle in radians:"))
        print(f"The answer is: {math.cos(value_one)}")
        break

    # Tangent
    elif oper == "9":
        value_one = float(input("\nEnter the angle in radians:"))
        print(f"The answer is: {math.tan(value_one)}")
        break

import math


while True:
    print("\n=======================================================\n                      Sci-Calc\n=======================================================\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raise to nth power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n=======================================================")

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

    # Subtraction
    elif oper == "1":
        value_one = float(input("\nFirst value: "))
        value_two = float(input("\nSecond value: "))
        print(f"The answer is: {value_one - value_two}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break


    # Multiplication
    elif oper == "2":
        value_one = float(input("\nFirst value: "))
        value_two = float(input("\nSecond value: "))
        print(f"The answer is: {value_one * value_two}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break

    
    # Division
    elif oper == "3":
        value_one = float(input("\nFirst value: "))
        value_two = float(input("\nSecond value: "))
        print(f"The answer is: {value_one / value_two}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break

        
    # Modulo
    elif oper == "4":
        value_one = float(input("\nFirst value: "))
        value_two = float(input("\nSecond value: "))
        print(f"The answer is: {value_one % value_two}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break

        
    # Raise to nth power
    elif oper == "5":
        value_one = float(input("\nFirst value: "))
        value_two = float(input("\nPower to raise to: "))
        print(f"The answer is: {value_one ** value_two}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break

        
    # Square root
    elif oper == "6":
        value_one = float(input("\nFind the square root of: "))
        print(f"The answer is: {math.sqrt(value_one)}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break


    # Logarithm
    elif oper == "7":
        value_one = float(input("\nEnter value: "))
        base = float(input("\nBase of the logarith : "))
        print(f"The answer is: {math.log(value_one, base)}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break


    # Sine
    elif oper == "8":
        value_one = float(input("\nEnter the angle in degrees: "))
        print(f"The answer is: {math.sin(value_one)}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break
        

    # Cosine
    elif oper == "9":
        value_one = float(input("\nEnter the angle in degrees: "))
        print(f"The answer is: {math.cos(value_one)}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break

        
    # Tangent
    elif oper == "10":
        value_one = float(input("\nEnter the angle in degrees: "))
        print(f"The answer is: {math.tan(value_one)}")
        
        go_back = input("\nGo back to the main menu? (Y/N): ")
        if go_back.upper() == "Y":
            continue
        else:
            break
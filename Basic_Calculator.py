import math 

history = []

while True :
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Addition")
    print("2. Difference")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. View History")
    print("9.Clear History")
    print("10. Exit")

    choice = input("\nEnter your Choice(1-10) : ")

    if choice =='1':
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        result = 0
        for num in numbers:
            result+=num
        history.append(f"{' + '.join(map(str, numbers))} = {result}")
        print(f'Result : {result}')

    elif choice == '2':
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        result = numbers[0]
        for num in numbers[1:]:
            result-=num
        history.append(f"{' - '.join(map(str, numbers))} = {result}")
        print(f'Result : {result}')

    elif choice == '3':
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        result=1
        for num in numbers:
            result*=num
        history.append(f"{' * '.join(map(str, numbers))} = {result}")
        print(f'Result : {result}')

    elif choice =='4' :
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]
        result = numbers[0]
        valid = True
        for num in numbers[1:]:
            if num==0:
                print("Cannot Divide bty Zero")
                valid = False
                break
            result/=num
        if valid:
            print(f'Result : {result}')
        history.append(f"{' / '.join(map(str, numbers))} = {result}")
        
    elif choice == '5':
        base=float(input("Enter the Number : "))
        exponent=float(input("Enter the Power : "))
        result=base**exponent
        history.append(f"{base}^{exponent} = {result}")
        print(f'Result : {result}')

    elif choice == '6':
        number=float(input("Enter the Number : "))
        if number<0:
            print("Square root of Negative Number is not Possible.")
        else:
            result=math.sqrt(number)
            print(f'Result : {result}')
        history.append(f"√{number} = {result}")

    elif choice =='7':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Modulus with Zero is not Possible.")
        else:
            result = num1 % num2
            print(f'Result : {result}')
        history.append(f"{num1} % {num2} = {result}")

    elif choice == '8':
        if len(history) == 0:
            print("\nNo calculations yet.")
        else:
            print("\n========== HISTORY ==========")
            for calculation in history:
                print(calculation)

    elif choice =='9':
        history.clear()
        print("History Clear")

    elif choice =='10':
        print("Thank you for using the Calculator.")
        break

    else:
        print("Invalid Choice!")

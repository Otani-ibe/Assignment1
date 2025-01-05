print("\n                                    WEEK ONE ASSIGNMENT!")
numbers = []

while True:
    user_choice = input("\nType enter, show, see result, number type, restart or exit: ").strip()

    match user_choice:
        case "enter":
            first_num = int(input("Enter first number: "))
            print(f"Good Job! {first_num} has been added")
            numbers.append(first_num)

            while True:
                second_number = int(input("Enter Second Number: "))
                if second_number > first_num:
                    print(f"Good Job! {second_number} has been added")
                    numbers.append(second_number)
                    break
                else:
                    print(f"\nSorry! Second number must be greater than first number.")
                    print(f"Example: number {second_number} must be greater than {first_num}")


            while True:
                third_number = int(input("Enter third number: "))
                if third_number > second_number or first_num:
                    print(f"Good Job! {third_number} has been added")
                    numbers.append(third_number)
                    break
                else:
                    print(f"\nSorry! Third number must be greater than second and first number.")
                    print(f"Example: number {third_number} must be greater than {second_number} and {first_num}")

        case "show":
            print("\nThe numbers entered are:")
            for number in numbers:
                print(number)

        case "see result":
            add_number = first_num + second_number + third_number
            subtract_number = third_number - second_number - first_num
            multiply_number = third_number * second_number * first_num

            print(f"\nAddition of numbers = ({add_number})")
            print(f"\nSubtraction of numbers in DESCENDING order = ({subtract_number})")
            print(f"\nMultiplication of numbers in DESCENDING order = ({multiply_number})")

        case "number type":
            if first_num % 2 == 0:
                print(f"First number ({first_num}) is even")
            else:
                print(f"First number ({first_num}) is odd")

            if second_number % 2 == 0:
                print(f"second number ({second_number}) is even")
            else:
                print(f"Second number ({second_number}) is odd")

            if third_number % 2 == 0:
                print(f"Third number ({third_number}) is even")
            else:
                print(f"Third number ({third_number}) is odd")


        case "restart":
            print("Restarting the application..")
            numbers = []

        case "exit":
            print("Goodbye!")
            break










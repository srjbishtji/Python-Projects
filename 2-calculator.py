# CORE LOGIC

def show_menu():
    print("\nSelect 1 for Addition (+)")
    print("Select 2 for Subtraction (-)")
    print("Select 3 for Multiplication (*)")
    print("Select 4 for Float Division (/)")
    print("Select 5 for Integer Division (//)")
    print("Select 6 for Exponent (**)")
    print("Select 7 for Remainder (%)")

def calculation(a,b,option):
            if option == 1:
                return a + b 
            elif option == 2:
                return a - b
            elif option == 3: 
                return a*b
            elif option == 4:
                return a/b
            elif option == 5:
                return a//b
            elif option == 6:
                return a**b
            elif option == 7:
                return a%b
            else:
                return "Choose an option"
            
while True:
    show_menu()
    try:
        # numbers = map(int,input("enter the numbers : ").split(","))
        numbers = input("Enter two numbers comma separated or type 'history' to view past calculations: ").strip()
        
        if numbers.lower() == "history":
            try:
                with open("calculation_history.txt", "r") as file:
                    history = file.read()
                    if history:
                        print("\n--- Calculation History ---")
                        print(history)
                    else:
                        print("No history found.")
            except FileNotFoundError:
                print("History file does not exist yet.")
            continue
        
        nums = numbers.split(",")
        if len(nums) != 2:
            print("Please enter exactly two numbers separated by a comma.")
            continue
    
        a, b = map(float, nums)
        
        option = int(input("enter the Choice : "))
        
        if b == 0 and (option == 4 or option == 5 or option == 7):
            raise ZeroDivisionError("Cannot divide by zero.")
            
        if option not in range(1,8):
             print("Invalid choice! Please select a number from 1 to 7")
             
        calci = calculation(a,b,option)
        print(f"Result: {calci}")

        again = input('enter "yes" to continue : ').lower()
        with open("calculation_history.txt", "a") as file:
            result = f"Numbers is : {a}, {b} and option is : {option} and The calculation is : {calci}\n"
            file.write(result)
       
        if again == "yes":
            continue
        else:
            print("Program Ended")
            break

        
    except ValueError:
        print("Invalid input! Please enter two numbers separated by a comma, like 4,5.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
# CORE LOGIC

print("Select 1 for Addition (+)")
print("Select 2 for Subtraction (-)")
print("Select 3 for Multiplication (*)")
print("Select 4 for FLoat Division (/)")
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
    try:
        numbers = input("enter the numbers : ").split(",")
        option = int(input("enter the Choice : "))
        print(calculation(*numbers, option))

        again = input("enter yes to continue : ").lower()
        if again == "yes":
            continue
        else:
            break
    except ValueError:
        print("Invalid input! Please enter two numbers separated by a comma, like 4,5.")

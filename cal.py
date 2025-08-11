print("PYTHON CALCULATOR")



choice = input("choose [+ , - , * ,/]: ")
if choice == '+':
    num1 = int(input("enter the 1st number: "))
    num2 = int(input("enter the 2nd number: "))
    total = (num1) + (num2)
    print(f"{num1} + {num2} = {total}")
elif choice == '-':
    num1 = int(input("enter the 1st number: "))
    num2 = int(input("enter the 2nd number: "))
    total = (num1) - (num2)
    print(f"{num1} - {num2} = {total}")
elif choice == '*':
    num1 = int(input("enter the 1st number: "))
    num2 = int(input("enter the 2nd number: "))
    total = (num1) * (num2)
    print(f"{num1} * {num2} = {total}")
elif choice == '/':
    num1 = int(input("enter the 1st number: "))
    num2 = int(input("enter the 2nd number: "))
    total = (num1) / (num2)
    print(f"{num1} / {num2} = {total}")
else:
    print("invalid , choose again [+ , - , * ,/]: ")

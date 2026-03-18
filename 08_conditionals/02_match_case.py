# switch case statement
a=int(input("Enter your lucky number between 1 and 10: "))

match(a):
    case 1:
        print("You won the charger")
    case 3:
        print("You won the camera")
    case 6:
        print("You won the charger")
    case _:
        print(f"The value is {a} . Better luck next time !!!")
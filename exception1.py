try:
    num = int(input("Enter the number:"))
    result = 10 / num

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by Zero")
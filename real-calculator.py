def add(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose"))

if choice == 1:
    print(add(num1,num2))
elif choice ==2:
    print(substract(num1,num2))
elif choice == 3:
    print(multiply(num1,num2))
elif choice == 4:
    print(divide(num1,num2))
else:
    print("Invalid Option....")
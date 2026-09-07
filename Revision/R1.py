name = input("Enter the name:")

n = int(input("Enter the number of subject:"))
avg = 0
total = 0
for i in range(n):
    marks = int(input("Enter the marks:"))

    total = total+marks


print("total",total)
avg = total/n
print("Average",avg)

if avg >= 80:
    print("Excellent")

elif avg >=60:
    print("Good")

elif avg >= 40:
    print("pass")

elif avg < 40:
    print("Fail")
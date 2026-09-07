marks = [78, 45, 92, 33, 67, 88]
passed = 0
failed = 0
for mark  in marks :
    print(mark)

    if mark >= 40:
        print("passed")
        passed = passed +1

    else:
        print("failed")
        failed = failed +1

Total = len(marks)

print (f"Total Student: {Total} \n Passed : {passed} \n Failed: {failed}")
print("Total Students :",Total)
print("passed",passed)
print("Failed",failed)
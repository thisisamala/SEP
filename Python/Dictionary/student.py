n = int(input("How many items? "))
student_record = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student_record[key] = value

print(student_record)
query=input("enter the name of the student whose mark is to be retrieved ")
grade=(student_record.get(query))
if grade is None:
    print(query,"is not found in the records")
else:
    print(query+"'s grade is",grade)
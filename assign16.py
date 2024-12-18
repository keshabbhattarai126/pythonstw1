students = int(input("Enter the number of students: "))
apples = int(input("Enter the number of apples: "))

apples_distributed = 0
apples_remaining = apples

for i in range(students):
    if apples_remaining > 0:
        apples_distributed += 1
        apples_remaining -= 1

apples_per_student = apples // students
apples_left = apples % students

print(f"Each student gets {apples_per_student} apples.")
print(f"The number of apples remaining in the basket is {apples_left}.")

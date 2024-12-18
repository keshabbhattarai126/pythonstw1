no_of_std_class_a = int(input("Enter the number of students in class A: "))
no_of_std_class_b = int(input("Enter the number of students in class B: "))
no_of_std_class_c = int(input("Enter the number of students in class C: "))


classes = {
    "Class A": no_of_std_class_a,
    "Class B": no_of_std_class_b,
    "Class C": no_of_std_class_c
}

total_desks = 0

for class_name, no_of_students in classes.items():
   
    if no_of_students % 2 == 0:
        desks = no_of_students // 2
    else:
        desks = (no_of_students // 2) + 1
   
    total_desks += desks


print(f"The smallest possible number of desks to be purchased is: {total_desks}")

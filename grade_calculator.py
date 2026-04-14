total = 0

name = input("enter your name: ")
print("hello", name)

num_subjects = int(input("enter the number of subjects: "))
for i in range(num_subjects):
    subject_name = input("enter the name of subject: ")
    marks = int(input(f"enter the marks obtained in {subject_name}: "))
    total = total + marks

average = total / num_subjects

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nname: {name}")
print(f"total: {total}")
print(f"average: {average:.2f}")
print(f"grade: {grade}")
# Function to calculate the average of grades
def med(g):
    return sum(g) / len(g) if g else 0  # More efficient and avoids division by zero

# Empty lists to store user input
students = []
grades = []

# Get the number of students, with input validation
while True:
    try:
        class_number = int(input("How many students are in class? "))
        if class_number <= 0:
            raise ValueError("Number of students must be positive.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number.")

# Collect student names and grades
for _ in range(class_number):
    student = input("What's the student's name? ").strip().title()

    while True:
        try:
            grade = int(input(f"What is {student}'s grade? "))
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid grade.")

    students.append(student)
    grades.append(grade)

# Create dictionary of students and grades
final = dict(zip(students, grades))

# Calculate average
print(f"\nThe average grade was {med(grades):.2f}")

# Find highest and lowest grades with associated students
max_grade = max(grades)
min_grade = min(grades)

best_students = [s for s, g in final.items() if g == max_grade]
worst_students = [s for s, g in final.items() if g == min_grade]

print(f"The highest grade was {max_grade} by: {', '.join(best_students)}")
print(f"The lowest grade was {min_grade} by: {', '.join(worst_students)}")

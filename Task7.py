# Step 1: Create a dictionary of students and marks
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Dan": 49,
    "Emilia": 93,
    "Finn":57
}

# Step 2: Ask user for a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Check if student exists and display marks or a not found message
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")


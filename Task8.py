# Task 2: Write and Append Data to a File


with open("output.txt", "w") as file:
    user_input = input("Enter some data to write to the file: ")
    file.write(user_input + "\n")

with open("output.txt", "a") as file:
    additional_input = input("Enter additional data to append: ")
    file.write(additional_input + "\n")

print("\n Final content of 'output.txt':")
with open("output.txt", "r") as file:
    print(file.read())

# Experiment 3 - String, list and tuple methods
# Question: Store a student's name; display uppercase, lowercase, title case and character count.
# Theme: String methods and len().
name = input("Enter student's name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("Number of characters:", len(name))


# Experiment 3 - String, list and tuple methods
# Question: Create a list of five student names, display it, add a name, remove a name and sort alphabetically.
# Theme: List append(), remove() and sort().
students = ["Amit", "Rahul", "Priya", "Sneha", "Rohan"]
print("Original list:", students)

new_name = input("Enter a new student's name to add: ")
students.append(new_name)

remove_name = input("Enter a student's name to remove: ")
if remove_name in students:
    students.remove(remove_name)
else:
    print("Name not found; no item removed.")

students.sort()
print("Updated sorted list:", students)


# Experiment 3 - String, list and tuple methods
# Question: Store marks of five students; display marks, highest, lowest, total and ascending order.
# Theme: Lists and built-in max(), min(), sum(), sort().
marks = []
for i in range(5):
    marks.append(float(input(f"Enter marks of student {i + 1}: ")))

print("Marks:", marks)
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Total marks:", sum(marks))
marks.sort()
print("Marks in ascending order:", marks)


# Experiment 3 - String, list and tuple methods
# Question: Store five student roll numbers in a tuple; display all and the value at index 2.
# Theme: Tuple creation and indexing.
roll_numbers = (101, 102, 103, 104, 105)
print("Roll numbers:", roll_numbers)
print("Roll number at index 2:", roll_numbers[2])



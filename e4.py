# Experiment 4 - Set and dictionary methods
# Question: Create sensor sets for Robot A and Robot B; add Proximity to A and show common, union and A-only sensors.
# Theme: Set add(), intersection(), union() and difference().
robot_a = {"Temperature", "Pressure", "Humidity"}
robot_b = {"Humidity", "Ultrasonic", "Infrared"}

print("Robot A sensors:", robot_a)
print("Robot B sensors:", robot_b)

robot_a.add("Proximity")
print("Robot A after adding Proximity:", robot_a)
print("Common sensors:", robot_a.intersection(robot_b))
print("All sensors used by either robot:", robot_a.union(robot_b))
print("Sensors used by A but not B:", robot_a.difference(robot_b))


# Experiment 4 - Set and dictionary methods
# Question: Create Rahul's student dictionary; display it and name, add year=2, update department and display keys and values.
# Theme: Dictionary access, assignment, update(), keys() and values().
student = {
    "name": "Rahul",
    "department": "Mechatronics Engineering",
    "roll_number": 101
}

print("Complete dictionary:", student)
print("Student name:", student["name"])

student["year"] = 2
student["department"] = "Information Technology"

print("Updated dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())

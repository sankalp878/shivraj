# Experiment 8 - Built-in and user-defined functions
# Question: Process sensor readings 25, 30, 35, 40 using max(), min(), sum() and average_temperature().
# Theme: Built-in functions and a user-defined function.
readings = [25, 30, 35, 40]

def average_temperature(values):
    return sum(values) / len(values)

print("Sensor readings:", readings)
print("Maximum temperature:", max(readings))
print("Minimum temperature:", min(readings))
print("Total temperature:", sum(readings))
print("Average temperature:", average_temperature(readings))


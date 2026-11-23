# Experiment 9 - File handling: data streams, access modes, read/write
# Question: Write 70°C to sensor_data.txt, read it, append 75°C and display all readings.
# Theme: File modes w, r and a.
filename = "sensor_data.txt"

# Write the first sensor reading.
with open(filename, "w", encoding="utf-8") as file:
    file.write("Temperature: 70 C\n")
print("Sensor data saved successfully.")

# Read and display the stored reading.
with open(filename, "r", encoding="utf-8") as file:
    print("Stored data:")
    print(file.read(), end="")

# Append a second sensor reading without deleting the first.
with open(filename, "a", encoding="utf-8") as file:
    file.write("Temperature: 75 C\n")

# Display all readings.
with open(filename, "r", encoding="utf-8") as file:
    print("All sensor readings:")
    print(file.read(), end="")

# Experiment 10 - Object-Oriented Programming: Class and Objects
# Question: Create TemperatureSensor with sensor name and temperature; create two objects at 70°C and 85°C and display readings.
# Theme: Class, objects, __init__() and instance methods.

class TemperatureSensor:
    def __init__(self, sensor_name, temperature):
        self.sensor_name = sensor_name
        self.temperature = temperature

    def display_reading(self):
        print("Sensor Name:", self.sensor_name)
        print("Temperature:", self.temperature, "C")


sensor1 = TemperatureSensor("Sensor 1", 70)
sensor2 = TemperatureSensor("Sensor 2", 85)

sensor1.display_reading()
print()
sensor2.display_reading()

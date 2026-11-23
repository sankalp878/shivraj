# Experiment 7 - break, pass and continue
# Question: Print numbers from 1 to 10 and stop when the number reaches 5.
# Theme: break statement.
for number in range(1, 11):
    if number == 5:
        break
    print(number)


# Experiment 7 - break, pass and continue
# Question: Print numbers from 1 to 10, skipping number 5.
# Theme: continue statement.
for number in range(1, 11):
    if number == 5:
        continue
    print(number)

# Experiment 7 - break, pass and continue
# Question: Print numbers from 1 to 5 and demonstrate pass when the number is 3.
# Theme: pass statement as a no-operation placeholder.
for number in range(1, 6):
    if number == 3:
        pass
    print(number)



# Experiment 5 - Conditional statements
# Question: Verify username and password using if-else. Ask for password only when username is correct.
# Theme: if-else decision making.
correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")

if username == correct_username:
    password = input("Enter password: ")
    if password == correct_password:
        print("Correct Password")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")

# Experiment 5 - Conditional statements
# Question: Simulate banking login for Rahul, Priya and Amit using the supplied usernames, passwords and balances.
# Theme: Conditional statements and dictionary-based account lookup.
accounts = {
    "rahul": {"password": "rahul123", "balance": 15000},
    "priya": {"password": "priya456", "balance": 25000},
    "amit": {"password": "amit789", "balance": 40000}
}

username = input("Enter username: ")

if username in accounts:
    password = input("Enter password: ")
    if password == accounts[username]["password"]:
        print("Login Successful")
        print("Account Balance: Rs.", accounts[username]["balance"])
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")

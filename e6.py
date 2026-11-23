# Experiment 6 - for and while loops
# Question: Rahul's bank login; repeat password prompt with while loop until correct. Show balance; reject wrong username.
# Theme: while loop and conditional statements.
username = input("Enter username: ")

if username == "rahul":
    password = ""
    while password != "rahul123":
        password = input("Enter password: ")
        if password != "rahul123":
            print("Incorrect Password. Try again.")

    print("Login Successful")
    print("Account Balance: Rs. 15000")
else:
    print("Incorrect Username")


# Experiment 6 - for and while loops
# Question: Rahul's bank login with a maximum of three password attempts using a for loop.
# Theme: for loop, range(), break and conditional logic.
username = input("Enter username: ")

if username == "rahul":
    for attempt in range(1, 4):
        password = input(f"Enter password (attempt {attempt}/3): ")
        if password == "rahul123":
            print("Login Successful")
            print("Account Balance: Rs. 15000")
            break
        else:
            print("Incorrect Password")
    else:
        print("Account Locked. Maximum Attempts Exceeded.")
else:
    print("Incorrect Username")

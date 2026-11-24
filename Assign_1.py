balance = 10000

pin = 2468

total_deposit = 0
total_withdrawal = 0

transactions = []

print("========== SECUREATM ==========")

attempts = 0
login = False

while attempts < 3:

    entered_pin = int(input("Enter PIN: "))

    if entered_pin == pin:

        print("Login successful!")
        login = True
        break

    else:

        print("Incorrect PIN!")
        attempts += 1

if login:

    while True:

        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("Available Balance: ₹{:.2f}".format(balance))

        elif choice == "2":

            amount = float(input("Enter deposit amount: "))

            if amount > 0:

                balance = balance + amount

                total_deposit = total_deposit + amount

                transactions.append(["Deposit", amount, balance])

                print("Deposit successful!")

                print("Updated Balance: ₹{:.2f}".format(balance))

            else:

                print("Invalid deposit amount!")

        elif choice == "3":

            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:

                print("Invalid withdrawal amount!")

            elif amount > balance:

                print("Insufficient balance!")

            else:

                balance = balance - amount

                total_withdrawal = total_withdrawal + amount

                transactions.append(["Withdrawal", amount, balance])

                print("Withdrawal successful!")

                print("Updated Balance: ₹{:.2f}".format(balance))


        elif choice == "4":

            print("\n--- TRANSACTION HISTORY ---")

            if len(transactions) == 0:

                print("No transactions found.")

            else:

                for t in transactions:

                    print("Type:", t[0])

                    print("Amount: ₹{:.2f}".format(t[1]))

                    print("Balance: ₹{:.2f}".format(t[2]))

                    print("----------------------")

        elif choice == "5":

            print("\n--- TRANSACTION SUMMARY ---")

            print("Total Deposits: ₹{:.2f}".format(total_deposit))

            print("Total Withdrawals: ₹{:.2f}".format(total_withdrawal))

            print("Closing Balance: ₹{:.2f}".format(balance))

            print("Thank you for using SecureATM!")

            break

        else:

            print("Invalid choice! Please try again.")

else:

    print("Access denied. Too many incorrect attempts.")
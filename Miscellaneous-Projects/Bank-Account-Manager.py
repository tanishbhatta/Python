name = input("Enter your name: ").strip()
current_balance = float(input("Enter your current balance: "))
withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

if current_balance >= 0:
    if withdrawal_amount>0 and withdrawal_amount <= current_balance:
        print("Transaction Successfull!")
        new_balance = current_balance - withdrawal_amount
        print(f"Current Balance: {new_balance}")
        if new_balance >= 100_000:
            print("Account Status: Premium")
        elif 10_000 <= new_balance < 100_000:
            print("Account Status: Standard")
        else:
            print("Account Status: Low balance")
    else:
        print("Transaction Failed!")
else:
    print("Negative Balance Is Not Allowed!")
def log_transaction(transaction_id, 
                    user_id, 
                    / , 
                    *, 
                    currency,
                    amount, 
                    status="PENDING"):
    return f"{transaction_id} | {user_id} | {amount} | {currency} | {status}"

reciept = log_transaction(
    "TXN-991",
    "USR-22",
    currency="USD",
    amount=450.25
)

print(reciept)
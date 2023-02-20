import time
from sql_queries import get_transactions

if __name__ == '__main__':
    while True:
        total_amount = sum(transaction.amount for transaction in get_transactions())
        print(f"Total amount: {total_amount}")
        time.sleep(16)

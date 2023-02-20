import time
from sql_queries import get_transactions

if __name__ == '__main__':
    while True:
        transactions = get_transactions()
        print("All transactions:")
        for transaction in transactions:
            print(f"{transaction.description}, price: {transaction.price}, quantity: {transaction.quantity}, amount: {transaction.amount}")
        time.sleep(11)

#отображает все транзакции в базе данных по price, quantity, amount.
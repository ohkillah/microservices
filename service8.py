import time
from sql_queries import get_transactions, update_transactions

if __name__ == '__main__':
    while True:
        transactions = get_transactions()
        for transaction in transactions:
            if transaction.status == 'new':
                update_transactions()
        time.sleep(17)

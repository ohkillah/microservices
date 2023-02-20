import time
from sql_queries import get_transactions

if __name__ == '__main__':
    while True:
        transactions = get_transactions()
        print(transactions)
        time.sleep(25)

#выполняет запрос на получение всех транзакций, находящихся в таблице
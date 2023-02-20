import time
from sql_queries import create_table

if __name__ == '__main__':
    create_table()
    print("Table created.")
    while True:
        time.sleep(12)


#создает таблицу в базе данных
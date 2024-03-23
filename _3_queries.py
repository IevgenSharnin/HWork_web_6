import sqlite3

def execute_query(sql):

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який виконає запит
        cur.execute(sql)
        return cur.fetchall()


if __name__ == "__main__":
    # читаємо файл зі скриптом запиту
    with open('query_3.sql', 'r') as f:
        sql = f.read()
    print (execute_query(sql))

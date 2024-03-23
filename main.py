from _1_create_tables import create_db 
from _2_fill_tables_by_faker import fill_db
from _3_queries import execute_query

queries = []
queries.append ("1) Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
queries.append ("2) Знайти студента із найвищим середнім балом з певного предмета.")
queries.append ("3) Знайти середній бал у групах з певного предмета.")
queries.append ("4) Знайти середній бал на потоці (по всій таблиці оцінок).")
queries.append ("5) Знайти які курси читає певний викладач.")
queries.append ("6) Знайти список студентів у певній групі.")
queries.append ("7) Знайти оцінки студентів у окремій групі з певного предмета.")
queries.append ("8) Знайти середній бал, який ставить певний викладач зі своїх предметів.")
queries.append ("9) Знайти список курсів, які відвідує студент.")
queries.append ("10) Список курсів, які певному студенту читає певний викладач.")
queries.append ("11) Середній бал, який певний викладач ставить певному студентові.")
queries.append ("12) Оцінки студентів у певній групі з певного предмета на останньому занятті.")

if __name__ == "__main__":
    print ("Створюємо базу даних оцінювання студентів із рандомними даними")
    create_db()
    fill_db()
    print ('\nДля виведення доступні наступні запити:')
    for query in queries:
        print (query)
    
    number = input ('\nВведіть номер запиту або щось інше для виходу: ')
    print ('Якщо у запиті "певний" чи "окремий", виводжу по першому значенню у базі.\n')
    try:
        if int (number) in range (1, 12+1):
            filename = f'query_{int(number)}.sql'
            with open(filename, 'r') as f:
                sql = f.read()
            list_of_answers = execute_query(sql)
            for row_number in list_of_answers:
                print (row_number)
    except: pass

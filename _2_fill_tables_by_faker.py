from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 33
NUMBER_TEACHERS = 5
NUMBER_COURSES = 8
NUMBER_GRADES_FOR_EACH_STUDENT = 20


def generate_fake_data(number_groups, number_students, number_teachers, number_courses) -> tuple():
    fake_groups = []  # тут зберігатимемо компанії
    fake_students = []  # тут зберігатимемо студентів
    fake_teachers = []  # тут зберігатимемо вчителів
    fake_courses = [] # тут курси-предмети
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    # Створимо набір груп 
    for gr in range(number_groups):
        fake_groups.append(f'group_{gr+1}')

    # Згенеруємо студентів та викладачів
    for _ in range(number_students):
        fake_students.append(fake_data.name())
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # Та number_post набір посад
    for _ in range(number_courses):
        fake_courses.append(fake_data.job())

    return fake_groups, fake_students, fake_teachers, fake_courses


def prepare_data(groups, students, teachers, courses) -> tuple():
    for_groups = []
    # готуємо список кортежів назв груп
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    # готуємо список кортежів назв викладачів
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_students = []  # для таблиці студентів
    for student in students:
        # Для записів у таблицю студентів додаємо групу, випадкову за id
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_courses = []  # для таблиці курсів
    for course in courses:
        # Для записів у таблицю предметів додаємо викладача, випадкового за id
        for_courses.append((course, randint(1, NUMBER_TEACHERS)))
    '''
    Для запису у таблицю оцінок треба:
     - власне оцінку (рандом 2..5), 
     - дату (приймаємо перший семестр 2023-2024 навчального року, тобто рандом вересень-грудень),
     - студента (рандом 1..NUMBER_STUDENTS) 
     - курс (рандом 1..NUMBER_COURSES)
    Повинно бути 20 оцінок у кожного студента
    '''
    for_grades = []

    for stud_ in range (1, NUMBER_STUDENTS + 1):
        for _ in range (1, NUMBER_GRADES_FOR_EACH_STUDENT + 1):
            grade_date = datetime(2023, randint (9, 12), randint(1, 30)).date()
            # Виконуємо цикл за кількістю співробітників
            for_grades.append((randint(2, 5), grade_date, stud_, randint (1, NUMBER_COURSES) ))

    return for_groups, for_students, for_teachers, for_courses, for_grades


def insert_data_to_db(groups, students, teachers, courses, grades) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('university.db') as con:

        cur = con.cursor()

        '''Заповнюємо таблицю груп. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, 
        відзначимо знаком заповнювача (?) '''
        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        '''Для вставлення відразу всіх даних скористаємося методом executemany курсора. 
        Першим параметром буде текст скрипта, а другим - дані (список кортежів).'''
        cur.executemany(sql_to_groups, groups)

        # Далі вставляємо дані про студентів. Напишемо для нього скрипт і вкажемо змінні
        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""
        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію
        cur.executemany(sql_to_students, students)

        # 3аповнюємо таблицю із викладачами
        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                              VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        # 3аповнюємо таблицю із курсами
        sql_to_courses = """INSERT INTO courses(course_name, teacher_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_courses, courses)

        # 3аповнюємо таблицю із курсами
        sql_to_grades = """INSERT INTO grades(grade_value, date_of, student_id, course_id)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        # Фіксуємо наші зміни в БД
        con.commit()

def fill_db():
    groups, students, teachers, courses, grades = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_COURSES))
    insert_data_to_db(groups, students, teachers, courses, grades)
    print ('Таблички успішно заповнено рандомними даними:')
    print (f' - {NUMBER_GROUPS} груп(-и);')
    print (f' - {NUMBER_STUDENTS} студентів;')
    print (f' - {NUMBER_TEACHERS} викладачів;')
    print (f' - {NUMBER_COURSES} предметів;')
    print (f' - {NUMBER_GRADES_FOR_EACH_STUDENT * NUMBER_STUDENTS} оцінок.')

if __name__ == "__main__":
    fill_db()
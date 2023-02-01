import mysql.connector as mc
import datetime
import connection

def insert_user(cnx, user_data: dict):
    """
    Add user to database
    """
    cursor = cnx.cursor()
    add_user = ("INSERT INTO users (firstname, lastname, username,"
    "password, email) VALUES (%s, %s, %s, %s, %s)")
    data = (user_data['firstname'], user_data['lastname'],
            user_data['username'], user_data['password'], user_data['email'])

    cursor.execute(add_user, data)

    cnx.commit()

    cursor.close()

def insert_assignment(cnx, assignment_data: dict):
    """
    Add assignment to database
    """
    cursor = cnx.cursor()
    add_assignment = ("INSERT INTO assignments (username, due_dt, diff, assignment_name, time_needed) VALUES (%s, %s, %s, %s, %s)")

    data = (assignment_data['username'], assignment_data['due_dt'],
            assignment_data['diff'], assignment_data['assignment_name'], 
            assignment_data['time_needed'])

    cursor.execute(add_assignment, data)

    cnx.commit()

    cursor.close()

def insert_exam(cnx, exam_data: dict):
    """
    Add exam to database
    """
    cursor = cnx.cursor()
    add_exam = ("INSERT INTO exams (username, exam_dt) VALUES (%s, %s)")

    data = (exam_data['username'], exam_data['exam_dt'])

    cursor.execute(add_exam, data)

    cnx.commit()

    cursor.close()

def insert_event(cnx, event_data: dict):
    """
    Add event to database
    """
    cursor = cnx.cursor()
    add_event = ("INSERT INTO events (username, start_dt, end_dt, assignment_name) VALUES (%s, %s, %s, %s)")

    data = (event_data['username'], event_data['start_dt'], event_data['end_dt'], event_data['assignment_name'])

    cursor.execute(add_event, data)

    cnx.commit()

    cursor.close()

def format_dt(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def main():
    cnx = connection.establish_connection()
    
    exam = {'username': 'hank', 'exam_dt': format_dt(datetime.datetime.now())}
    insert_exam(cnx, exam)

    event = {'username': 'hank', 'start_dt': format_dt(datetime.datetime.now()), 'end_dt': format_dt(datetime.datetime.now()), 'assignment_name': 'stuff'}

    cnx.close()

if __name__ == '__main__':
    main()
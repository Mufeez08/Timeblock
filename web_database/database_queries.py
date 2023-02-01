import mysql.connector as mc
import connection

def fetch_user_data(cnx, username):
    """
    Find user data for username.
    """
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT * FROM users WHERE username = %s")
    cursor.execute(query, (username,))

    res = cursor.fetchall()

    if len(res) == 0:
        return False, {}

    if len(res) > 1:
        return False, {}

    cursor.close()

    return True, res[0]

def fetch_assignment_data(cnx, username):
    """
    Fetch all assignment data associated with username.
    """
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT * FROM assignments WHERE username = %s")
    cursor.execute(query, (username,))

    res = cursor.fetchall()
    
    cursor.close()

    return res

def fetch_exam_data(cnx, username):
    """
    Fetch all exam data associated with username.
    """
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT * FROM exams WHERE username = %s")
    cursor.execute(query, (username,))

    res = cursor.fetchall()

    cursor.close()

    return res

def fetch_event_data(cnx, username):
    """
    Fetch all event data associated with username.
    """
    cursor = cnx.cursor(dictionary=True)
    query = ("SELECT * FROM events WHERE username = %s")
    cursor.execute(query, (username,))

    res = cursor.fetchall()

    cursor.close()

    return res

def main():
    cnx = connection.establish_connection()

    username = input('Username: ').strip()

    print("User Data:\n", fetch_user_data(cnx, username))
    print("Assignment Data:\n", fetch_assignment_data(cnx, username))
    print("Exam Data:\n", fetch_exam_data(cnx, username))
    print("Event Data:\n", fetch_event_data(cnx, username))

    cnx.close()

if __name__ == "__main__":
    main()
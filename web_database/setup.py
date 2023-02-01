import mysql.connector

def get_connection(sql_username, sql_password):
    print("Attempting to Connect To MySQL server.\n")
    cnx = mysql.connector.connect(host='localhost', user=sql_username,
        password=sql_password)
    print("Connected.\n")
    return cnx

def store_user_sql_connection(username, password):
    with open('.sql_login.txt', 'w') as fp:
        sql_data = "{}\n{}".format(username, password)
        fp.write(sql_data)

def setup_database(cnx): 
    cursor = cnx.cursor()
    print("Attempting to setup database.\n")
    add_database = ("CREATE DATABASE website_data")
    cursor.execute(add_database)

    cursor.close()

    print("Database setup complete.\n")

def setup_tables(cnx):
    cursor = cnx.cursor()
    use_database = "USE website_data"
    cursor.execute(use_database)
    print("Attempting to setup tables.\n")

    TABLES = {}

    TABLES['users'] = ("CREATE TABLE users (firstname varchar(20) NOT NULL,"
    "lastname varchar(20) NOT NULL, username varchar(20) NOT NULL,"
    "password varchar(20) NOT NULL, email varchar(280) NOT NULL,"
    "PRIMARY KEY (username))")
    
    TABLES['assignments'] = ("CREATE TABLE assignments ("
    "username varchar(20) NOT NULL, due_dt datetime NOT NULL,"
    "diff char(1) NOT NULL, assignment_name varchar(80) NOT NULL,"
    "time_needed TIME NOT NULL)")

    TABLES['exams'] = ("CREATE TABLE exams (username varchar(20) NOT NULL,"
    "exam_dt datetime NOT NULL)")

    TABLES['events'] = ("CREATE TABLE events (username varchar(20) NOT NULL,"
    "start_dt datetime NOT NULL, end_dt datetime NOT NULL, assignment_name"
    " varchar(50) NOT NULL)")

    for table_name in TABLES:
        print("Attempting To Create {} Table\n".format(table_name))
        cursor.execute(TABLES[table_name])
        print("{} Table Created\n".format(table_name))

    print("Table Setup Complete.\n")
    cursor.close()

def insert_default_user(cnx):
    cursor = cnx.cursor()
    print("Attempting To Insert Default User.\n")
    add_user = ("INSERT INTO users (firstname, lastname, username, password, email) VALUES (%s, %s, %s, %s, %s)")
    user_data = ('Mufeez', 'Mulbagal', 'Mufeez', '123', 'mufeez08@gmail.com')

    cursor.execute(add_user, user_data)

    cnx.commit()
    print("Default User Inserted.")
    cursor.close()

def main():
    sql_username = input("SQL Username: ").strip()
    sql_password = input("SQL Password: ").strip()

    cnx = get_connection(sql_username, sql_password)
    store_user_sql_connection(sql_username, sql_password)
    setup_database(cnx)
    setup_tables(cnx)

    insert_default_user(cnx)

    cnx.close()

if __name__ == "__main__":
    main()

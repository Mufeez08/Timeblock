import mysql.connector as mc



def establish_connection():
    """
    Connect into the database.
    """
    cnx = None
    with open('.sql_login.txt', 'r') as fp:
        username, password = fp.readlines()
        cnx = mc.connect(user=username, password=password, 
                    database="website_data", host="localhost")
    print("connection successful!")
    return cnx


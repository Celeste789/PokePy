import mysql.connector


def initialize_connection():
    try:
        my_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ami1"
        )
        if my_connection.is_connected():
            cursor = my_connection.cursor()
            print(f"You have connected successfully")

            cursor = my_connection.cursor()
            create_database(cursor)
            create_table(cursor)

        return my_connection, cursor

    except Exception as error:
        print(f"Error {error}")


def create_database(cursor):
    cursor.execute("SHOW DATABASES")
    temp = cursor.fetchall()
    databases = [item[0] for item in temp]

    if "pokepy" not in databases:
        cursor.execute("CREATE DATABASE pokepy")

    cursor.execute("USE pokepy")


def create_table(cursor):
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]

    if "moves" not in tables:
        cursor.execute('''CREATE TABLE moves(
                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                name VARCHAR(100),
                power INT,
                pp INT
             )''')

    if "types" not in tables:
        cursor.execute('''CREATE TABLE types(
                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                name VARCHAR(100)                                        
        )''')

    if "weaknesses" not in tables:
        cursor.execute('''
                
        ''')


def close_connection(connection, cursor):
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

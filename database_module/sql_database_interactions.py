import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('test.db')

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Successfully created database!")
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, sql_command, data):
    #sql = ''' INSERT INTO projects(name,begin_date,end_date)
    #          VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql_command, data)
    conn.commit()
    return cur.lastrowid


if __name__ == '__main__':
    #create_connection(r"/Users/sadiela/Documents/courses_spring_2022/ec530/hospital-app/data/test.db")
    database = r"/Users/sadiela/Documents/courses_spring_2022/ec530/hospital-app/data/test.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    conn = create_connection()
    if conn is not None:
        create_table(conn, sql_create_projects_table)

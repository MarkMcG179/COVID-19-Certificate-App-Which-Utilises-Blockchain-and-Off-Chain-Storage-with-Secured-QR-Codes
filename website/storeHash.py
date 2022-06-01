from flask import session
import sqlite3
from sqlite3 import Error
from hashlib import sha256

db_file = "database.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_cert_by_id(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM cert WHERE id=?", (id,))

    rows = cur.fetchall()

    for row in rows:
        mystring = ''.join(map(str,row))
        hash = sha256(mystring.encode()).hexdigest()
        return hash

def main():
    database = r"C:\Users\portn\COVID-Flask-Web-App\website\database.db"

    # create a database connection
    conn = create_connection(database)
    id = session.get('user_id')
    with conn:
        return select_cert_by_id(conn, id)

if __name__ == '__main__':
    main()
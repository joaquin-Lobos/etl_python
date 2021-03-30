import sqlite3
import os


def create_schema():
    conn = sqlite3.connect('tabla.db')
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS Number;
            """)

    # Ejecutar una query
    c.execute(""" 
            CREATE TABLE Number(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [number] INTEGER NOT NULL
            );
            """)

    conn.commit()
    conn.close()


def insert_product(numero):
    conn = sqlite3.connect('tabla.db')
    c = conn.cursor()

    values = [numero]

    c.execute("""
        INSERT INTO Number (number)
        VALUES (?);""", values)

    conn.commit()
    conn.close()
    print(numero, "success")
    
def get_product():
    conn = sqlite3.connect('tabla.db')
    c = conn.cursor()

    c.execute("""SELECT * FROM Number;""")

    result = c.fetchone()

    

    conn.commit()
    conn.close()

    return result

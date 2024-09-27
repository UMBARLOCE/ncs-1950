import sqlite3 as sq
import os


def create_ncs_table():
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS ncs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ncs TEXT,
        html TEXT,
        r INTEGER,
        g INTEGER,
        b INTEGER,
        c INTEGER,
        m INTEGER,
        y INTEGER,
        k INTEGER,
        page INTEGER
        )""")
    print('Data base connected OK!')


def insert_ncs(*args):
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO ncs VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)",
            (args)
        )


def select_page(ncs: str):
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query = cur.execute(
            f"""SELECT page
            FROM ncs
            WHERE ncs LIKE '{ncs}'"""
        ).fetchone()[0]
    return query


def select_ncs_html() -> list[tuple]:
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query_list: list[tuple] = cur.execute(
            f"""SELECT ncs, html
            FROM ncs"""
        ).fetchall()
    return query_list


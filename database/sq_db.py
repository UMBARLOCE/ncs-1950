import sqlite3 as sq
import os


def create_ncs_table() -> None:
    """Создание БД.

    Используется в модуле parsing.py.
    Уже не актуально, так как БД залита в git.
    """
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
        page TEXT
        )""")
    print('Data base connected OK!')


def insert_ncs(*args) -> None:
    """Наполнение БД.

    Используется в модуле parsing.py.
    Уже не актуально, так как БД залита в git.
    """
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO ncs VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)",
            (args),
        )


def select_ncs_html() -> list[tuple]:
    """Выборка кодов по ncs и html.
    
    Используется в модуле generate_jpg.py.
    Актуально.
    """
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query_list: list[tuple] = cur.execute(
            f"""SELECT ncs, html
            FROM ncs"""
        ).fetchall()
    return query_list


def select_ncs_code_and_page_number_by_ncs_code(ncs: str) -> tuple[str]:
    """Выборка кода цвета и номера страницы по коду цвета.
    
    Используется в модуле main.py.
    Актуально.
    """
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query = cur.execute(
            f"""SELECT ncs, page
            FROM ncs
            WHERE ncs LIKE '{ncs}'"""
        ).fetchone()
    return query


def select_ncs_codes_by_page_number(page: str) -> list[str]:
    """Выборка кодов цвета на странице по номеру страницы.
    
    Используется в модуле main.py.
    Актуально.
    """
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query: list[str] = list(
            cur.execute(
                f"""
                SELECT page, ncs
                FROM ncs
                """,
            ).fetchall()
        )

    res = []
    # i: ('21, 33', '2005-G80Y')
    for i in query:
        pages = i[0].split(', ')
        if page in pages:
            res.append(i[1])

    return res

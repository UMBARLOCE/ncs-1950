import sqlite3 as sq
import os


def create_db_and_ncs_table() -> None:
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


def insert_into_ncs_table(*args) -> None:
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


def select_all_ncs_and_html() -> list[tuple]:
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


def select_ncs_and_pages_by_ncs(ncs: str) -> tuple[str]:
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

    return query  # ('0502-Y', '3, 7, 22')


def select_ncs_whiteness(ncs: str) -> list[str]:
    """
    """
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query: list[tuple[str]] = list(
            cur.execute(
                f"""
                SELECT ncs
                FROM ncs
                """,
            ).fetchall()
        )

    whiteness_list = [i[0] for i in query if ncs[2:] == i[0][2:]]
    whiteness_list.sort()
    ind = whiteness_list.index(ncs)
    left = whiteness_list[ind - 1] if ncs != whiteness_list[0] else None
    right = whiteness_list[ind + 1] if ncs != whiteness_list[-1] else None
    return left, right


def select_ncs_and_pages_by_page(page: str) -> list[tuple]:
    """Выборка кодов цвета на странице по номеру страницы.
    
    Используется в модуле main.py.
    Актуально.
    """
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query: list[str] = list(
            cur.execute(
                f"""
                SELECT ncs, page
                FROM ncs
                """,
            ).fetchall()
        )

    res = [i for i in query if page in i[1].split(', ')]
    return res  # [('0502-Y', '3, 7, 22'), ('0502-Y50R', '3'), ... ]

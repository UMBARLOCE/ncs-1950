import sqlite3 as sq
import os


def select_ncs(page: str) ->list[tuple]:
    with sq.connect(os.path.join('database', 'data_base.db')) as con:
        cur = con.cursor()
        query: list[str] = list(cur.execute(
            f"""
            SELECT page, ncs
            FROM ncs
            """,
        ))

    res = []
    for i in query:
        pages = i[0].split(', ')
        if page in pages:
            res.append(i[1])

    return res


res = select_ncs('3')
print(res)

"""Десктоп приложение для поиска страницы в веере NCS_1950."""

import tkinter as tk
import sqlite3


def search_in_db(event) -> None:
    """Выполняет поиск по базе данных и обновляет список предложений."""
    search_term: str = entry.get()

    cursor.execute(
        "SELECT ncs, page FROM ncs WHERE ncs LIKE ?", ("%" + search_term + "%",)
    )
    results: list[tuple[str, str]] = cursor.fetchall()

    listbox.delete(0, tk.END)
    for row in results:
        listbox.insert(tk.END, row[0].ljust(12, "_") + row[1])


def select_in_listbox(event) -> None:
    """Очищает listbox и поле entry при клике по listbox."""
    listbox.delete(0, tk.END)
    entry.delete(0, tk.END)


def set_entry_focus(event) -> None:
    """Ставит курсор в поле entry."""
    entry.focus_set()


root = tk.Tk()  # создание главного окна
root.overrideredirect(False)  # включение/выключение рамки главного окна
root.title("NCS_1950")  # надпись в заголовке окна
root.resizable(False, False)  # запрет на изменение размеров окна
root.attributes("-topmost", True)  #  поверх всех окон
root.geometry("300x300+0+0")  #  размер и положение главного окна
root.option_add("*Font", ("Helvetica", 18))  # тип и размер шрифта глобально
root.bind("<FocusIn>", set_entry_focus)  # при активном окне курсор в поле entry


entry = tk.Entry(root, width=30)
entry.pack()
entry.bind("<KeyRelease>", search_in_db)


listbox = tk.Listbox(root, width=30, height=15)
listbox.pack()
listbox.bind("<<ListboxSelect>>", select_in_listbox)


conn = sqlite3.connect("./db.db")
cursor = conn.cursor()


root.mainloop()
conn.close()

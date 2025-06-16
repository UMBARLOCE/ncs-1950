"""
Десктоп приложение для поиска цветов NCS.
"""

import tkinter as tk
import sqlite3


def search_suggestions(event=None):
    """
    Выполняет поиск по базе данных и обновляет список предложений.
    """
    search_term = entry.get()
    cursor.execute(
        "SELECT ncs, page FROM ncs WHERE ncs LIKE ?", ("%" + search_term + "%",)
    )
    results = cursor.fetchall()

    listbox.delete(0, tk.END)
    for row in results:
        listbox.insert(tk.END, "\t\t".join(row))


def select_suggestion(event):
    """
    Обрабатывает выбор элемента из списка и вставляет его в поле ввода.
    """
    try:
        selected_index = listbox.curselection()[0]
        selected_suggestion = listbox.get(selected_index)
        entry.delete(0, tk.END)
        entry.insert(0, selected_suggestion)
        listbox.delete(0, tk.END)  # Очистка списка после выбора
    except IndexError:
        pass  # Ничего не выбрано


# Создание главного окна
root = tk.Tk()
root.title("NCS_1950")

# Поле ввода
entry = tk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", search_suggestions)

# Список предложений
listbox = tk.Listbox(root)
listbox.pack()
listbox.bind("<<ListboxSelect>>", select_suggestion)

# Подключение к базе данных SQLite3
conn = sqlite3.connect("./db.db")
cursor = conn.cursor()

root.mainloop()

# Закрытие соединения с базой данных при закрытии окна
conn.close()

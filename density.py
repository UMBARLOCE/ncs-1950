"""Приложение для расчета массы краски от плотности и объема."""

import tkinter as tk
from tkinter import ttk

COL = 4

interior_paint_dict: dict[str, float] = {
    "Armonia bi": 1.58,
    "Armonia deep": 1.46,
    "Maggiore bi": 1.38,
    "Maggiore tr": 1.18,
    "Opera bi": 1.54,
}


class Material(tk.Tk):
    """Класс оконного приложения."""

    def __init__(self) -> None:
        tk.Tk.__init__(self)

        self.title("Плотность")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        self.entry = tk.Entry(self, width=20)
        self.entry.pack()
        self.bind("<FocusIn>", func=lambda x: self.entry.focus_set())

        self.notebook = ttk.Notebook(self)
        self.notebook.pack()

        self.label = tk.Label(self)
        self.label.pack()

        self.set_interior_paint_frame()
        self.set_frame_facade_paint()

    def click_button(self, key) -> None:
        """Заглушка для проверки нажатия кнопки."""
        # print(f"Нажата кнопка {key}, значение: {interior_paint_dict[key]}")
        self.label.destroy()
        get_entry: str = self.entry.get()
        try:
            volume = float(get_entry.replace(",", "."))
        except:
            return
        weight: float = round(volume * interior_paint_dict[key], 3)
        self.label = tk.Label(self, text=f"{weight}")
        self.label.pack()

    def set_interior_paint_frame(self) -> None:
        """Создает фрейм для интерьерной краски."""

        self.interior_paint_frame = ttk.Frame(master=self.notebook)
        self.interior_paint_frame.pack()
        self.notebook.add(child=self.interior_paint_frame, text="Интерьерная")

        for i, key in enumerate(interior_paint_dict.keys()):
            row: int = i // COL
            col: int = i % COL
            btn = ttk.Button(
                master=self.interior_paint_frame,
                text=key,
                command=lambda k=key: self.click_button(k),
            )
            btn.grid(row=row, column=col)

        for i in range(COL):
            self.interior_paint_frame.grid_columnconfigure(index=i, weight=1)

    def set_frame_facade_paint(self) -> None:
        """Создает фрейм для фасадной краски."""
        self.facade_paint = ttk.Frame(master=self.notebook)
        self.facade_paint.pack()
        self.notebook.add(child=self.facade_paint, text="Фасадная")


def main() -> None:
    """Точка входа."""
    root = Material()
    root.mainloop()


if __name__ == "__main__":
    main()

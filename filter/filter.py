"""Фильтры для хендлеров."""


def is_number_from_1_to_216(msg):
    """Проверяет текст сообщения на число от 1 до 216."""
    return msg.text and msg.text.isdigit() and 0 < int(msg.text) < 217


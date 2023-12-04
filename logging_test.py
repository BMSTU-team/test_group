import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)  # Устанавливаем уровень логирования

def some_function(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        logging.warning("Введены не числовые значения!")

    logging.debug(f"Получены значения x={x} и y={y}")  # Логирование debug информации

    result = x + y

    return result

# Пример вызова функции
result = some_function(3, 5)
print(f"\nИтоговый результат: {result}\n\n")

# Пример вызова функции с неправильным вводом
result = some_function('abc', '5')  # Передаем строку вместо числа
print(f"\nИтоговый результат: {result}")

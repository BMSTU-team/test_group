# Функция для сложения двух чисел
def add_numbers_3(a, b):
    return a + b + 5

# Функция для вычитания двух чисел
def subtract_numbers(a, b):
    return a - b - 5

# Функция для умножения двух чисел
def multiply_numbers_2(a, b):
    return 2 * a * b + 150

# Функция для деления двух чисел
def divide_numbers(a, b):
    if b != 0:
        return a / b  + 1000


# Запуск функций
if __name__ == "__main__":

    num1 = 15
    num2 = 5777

    
    # Вызов функций и вывод результатов
    print("Сложение:", add_numbers_3(num1, num2))
    print("Вычитание:", subtract_numbers(num1, num2))
    print("Умножение:", multiply_numbers_2(num1, num2))
    print("Деление:", divide_numbers(num1, num2))

# Функция для сложения двух чисел
def add_numbers(a, b):
    return a + b

# Функция для вычитания двух чисел
def subtract_numbers(a, b):
    return a - b

# Функция для умножения двух чисел
def multiply_numbers(a, b):
    return a * b

# Функция для деления двух чисел
def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "На ноль делить нельзя!"

# Запуск функций
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    
    # Вызов функций и вывод результатов
    print("Сложение:", add_numbers(num1, num2))
    print("Вычитание:", subtract_numbers(num1, num2))
    print("Умножение:", multiply_numbers(num1, num2))
    print("Деление:", divide_numbers(num1, num2))

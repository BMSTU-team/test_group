# Калькулятор

def add(x, y):
    """Сложение двух чисел"""
    return float(x) + float(y)

def subtract(x, y):
    """Вычитание одного числа из другого"""
    return x - y

def multiply(x, y):
    """Умножение двух чисел"""
    return x * y

def divide(x, y):
    """Деление одного числа на другое"""
    if y == 0:
        raise ValueError("Деление на ноль невозможно")
    return x / y

# Пример использования калькулятора
result_add = add(10, 5)
result_subtract = subtract(10, 5)
result_multiply = multiply(10, 5)
result_divide = divide(10, 5)

print(f"Сложение: 10 + 5 = {result_add}")
print(f"Вычитание: 10 - 5 = {result_subtract}")
print(f"Умножение: 10 * 5 = {result_multiply}")
print(f"Деление: 10 / 5 = {result_divide}")

import random
import string

def generate_password(length=8):
    """
    Генерирует случайный пароль заданной длины.
    По умолчанию длина пароля — 8 символов.
    """
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Пример вызова функции
if __name__ == "__main__":
    print("=== Генератор паролей ===")
    try:
        length = int(input("Введите длину пароля: "))
        if length <= 0:
            print("Длина пароля должна быть больше 0! Установлено значение 8.")
            length = 8
    except ValueError:
        print("Ошибка: введите число! Установлено значение 8.")
        length = 8

    password = generate_password(length)
    print(f"\nВаш пароль: {password}")
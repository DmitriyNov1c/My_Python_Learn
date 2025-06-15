import random
import string

def generate_password(length=8, use_letters=True, use_digits=True, use_specials=True):
    """
    Генерирует пароль заданной сложности.
    
    Параметры:
    - length: длина пароля (по умолчанию 8)
    - use_letters: использовать буквы (A-Z, a-z)
    - use_digits: использовать цифры (0-9)
    - use_specials: использовать спецсимволы (!@#$%^&*())
    
    Возвращает:
    - Сгенерированный пароль или сообщение об ошибке, если ни один тип символов не выбран.
    """
    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += "!@#$%^&*()"
    
    if not chars:
        return "Ошибка: нужно выбрать хотя бы один тип символов!"
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    """Запрашивает у пользователя ответ 'да' или 'нет' (y/n)."""
    while True:
        answer = input(prompt + " (y/n): ").lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        print("Ошибка: введите 'y' (да) или 'n' (нет).")

if __name__ == "__main__":
    print("=== Улучшенный генератор паролей ===")
    
    # Запрос длины пароля
    try:
        length = int(input("Введите длину пароля: "))
        if length <= 0:
            print("Длина должна быть > 0. Установлено значение 8.")
            length = 8
    except ValueError:
        print("Некорректный ввод! Установлено значение 8.")
        length = 8
    
    # Запрос типов символов
    print("\nВыберите типы символов:")
    use_letters = get_yes_no_input("Использовать буквы (A-Z, a-z)?")
    use_digits = get_yes_no_input("Использовать цифры (0-9)?")
    use_specials = get_yes_no_input("Использовать спецсимволы (!@#$%^&*())?")
    
    # Генерация и вывод пароля
    password = generate_password(
        length=length,
        use_letters=use_letters,
        use_digits=use_digits,
        use_specials=use_specials
    )
    
    print("\n=== Ваш пароль ===")
    print(password)
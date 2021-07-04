from re import sub
from os import system
system("clear")

# Ф-ция для удаления всех знаков припинания и цифр из входящий строки
def d(string):
    return sub(r'[^\w\s]+|[\d]+', r'', string).strip()

def main():
    # Ввод исходной строки
    while True:
            try:
                string = input("Введите исходную строку: ")
                if len(string) <= 0:
                    system("clear")
                    print("Введите корректную строку")
                    continue
                break
            except ValueError:
                system("clear")
                print("Введите корректное значение")
                continue

    system("clear")
    print(f"Исходная строка: {string}")
    print(f"Преобразованная строка: {d(string)}")

if __name__ == "__main__":
    main()

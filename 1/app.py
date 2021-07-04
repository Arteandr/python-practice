from math import pi, pow
# Очистка терминала
from os import system
system("clear")

def main():
    # Ввод значений
    while True:
        try:
            r1 = float(input("Введите радиус верхнего основания: "))
            if r1 < 1:
                print("Радиус основания не может быть отрицательным")
                continue
            else:
                break
        except ValueError:
            system("clear")
            print("Введите корректное значение")
            continue

    while True:
        try:
            r2 = float(input("Введите радиус нижнего основания: "))
            if r2 < 1:
                print("Радиус основания не может быть отрицательным")
                continue
            else:
                break
        except ValueError:
            system("clear")
            print("Введите корректное значение")
            continue

    while True:
        try:
            h = float(input("Введите высоту: "))
            if h < 1:
                print("Высота не может быть отрицательная")
                continue
            else:
                break
        except ValueError:
            system("clear")
            print("Введите корректное значение")
            continue

    system("clear")
    print("Значения которые вы ввели: ")
    print(" Радиус верхнего основания: {} \n Радиус нижнего основания: {} \n Высота: {}".format(r1,r2,h))

    V = 1/3 * pi * h * (pow(r1,2) + r1*r2 + pow(r2,2))
    
    print("\nОбъем усеченного конуса: {:.3f}".format(V))



if __name__ == "__main__":
    main()

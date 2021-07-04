import csv
from os import system
system("clear")

header = ["Номер смеси", ["Состав смеси", ["Вода", "Изопропанол", "Олифа"]], "Температура возгорания"]

# Отрисовка разделителя
def printDel():
    print("-----------------------------------------------------------------------") 

# Отрисовка заголовка таблицы
def printHeader():
    printDel()
    print("| {:<10} | {:^28} | {:<10} |".format(header[0], header[1][0], header[2]))
    print("| {:<11} | {:<5} | {:<8} | {:<6} | {:<22} |".format(" ", header[1][1][0], header[1][1][1], header[1][1][2], " "))
    printDel()

# Отрисовка строки
def printRow(row):
    print("| {:^11} | {:^5} | {:^11} | {:^6} | {:^22} |".format(row[0], row[1], row[2], row[3], row[4]))

# Отрисовка всей таблицы
def printTable(data):
    printHeader()
    for i in data:
        printRow(i)
    printDel()

def getRight(data, s):
    newData = []
    for item in data:
        if item[4] >= s:
            newData.append(item)
    return newData

def main():
    try:
        # Открываем файл с данными
        with open('data.csv') as f:
            reader = csv.reader(f, delimiter='\t')
            data = [(int(col1), float(col2), float(col3), float(col4), float(col5))
                for col1, col2, col3, col4, col5 in reader]

        printTable(data) # Отрисовка таблицы

        # Проверка на ввод имени файла результата
        while True:
            outFile = input("Введите имя файла результата (.csv): ")
            if not outFile.replace(" ", "").endswith(".csv"):
                continue
            else:
                break

        while True:
            try:
                s = float(input("Введите температуру возгорания (S): "))
                break
            except ValueError:
                continue
        right = getRight(data, s)
        if len(right) <= 0:
            print("Подходящих смесей не найдено")
            exit(0)

        with open(outFile, 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            for item in right:
                writer.writerow(item)

        print(f"\nУ данных смесей температура возгорания не меньше {s}: ")
        printTable(right)

    except Exception as ex:
        print("Ошибка при открытии файла")
        print("Exception message: ",ex)
        exit(0)


if __name__ == "__main__":
    main()

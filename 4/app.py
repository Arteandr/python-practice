from account import Account
from money import Money
from os import system
system("clear")

accounts = []


def mainMenu():
    system("clear")
    print("1.Информация об объектах")
    print("2.Создать аккаунт")
    print("3.Снять деньги")
    print("4.Добавить деньги")
    print("5.Выйти")

    while True:
        try:
            key = int(input("\nВыберите вариант: "))
            if key < 1 or key > 5:
                continue
            else:
                break
        except:
            continue
    if key == 1:
        infoMenu()
    elif key == 2:
        addMenu()
    elif key == 3:
        subMoneyMenu()
    elif key == 4:
        addMoneyMenu()
    elif key == 5:
        system("clear")
        exit(0)
       
def addMoneyMenu():
    system("clear")
    if len(accounts) <= 0:
        mainMenu()
    while True:
        try:
            code = int(input("Введите идентификационный код желаемого аккаунта: "))
            exist = False
            for acc in accounts:
                if acc.code == code:
                    exist = True
                    currentAcc = acc

            if exist == False:
                continue
            else:
                break
        except:
            continue
    while True:
        try:
            summ = int(input("Введите желаемую сумму: "))
            if summ <= 0:
                continue
            else:
                break
        except:
            continue
    
    currentAcc.AddMoney(summ)
    mainMenu()

def subMoneyMenu():
    system("clear")
    if len(accounts) <= 0:
        mainMenu()
    while True:
        try:
            code = int(input("Введите идентификационный код желаемого аккаунта: "))
            exist = False
            for acc in accounts:
                if acc.code == code:
                    exist = True
                    currentAcc = acc

            if exist == False:
                continue
            else:
                break
        except:
            continue
    while True:
        try:
            summ = int(input("Введите желаемую сумму (0 чтобы выйти в меню): "))
            if summ < 0:
                continue
            elif summ == 0:
                mainMenu()
            else:
                res = currentAcc.SubMoney(summ)
                if res == -1:
                    print("Нет указанной суммы...")
                    continue
                else:
                    break
        except:
            continue
    mainMenu()

def infoMenu():
    if len(accounts) > 0:
        system("clear")
        for acc in accounts:
            acc.show()
            acc.m.show()
            if len(accounts) > 1:
                print("------------------------------------")
        input("\nДля продолжения нажмите любую клавишу...")
        mainMenu()
    else:
        mainMenu()


def addMenu():
    system("clear")
    while True:
        c = input("Введите название валюты: ")
        if len(c) <= 0:
            continue
        else:
            break

    m = Money(c, 0)
    while True:
        username = input("Введите имя пользователя: ")
        if len(username) <= 0:
            continue
        else:
            break

    while True:
        try:
            code = int(input("Введите идентификационный код: "))
            if code < 1:
                continue
            else:
                exist = False
                for acc in accounts:
                    if acc.code == code:
                        exist = True
                        break
                if exist:
                    print("\nУказанный идентификационный код уже используется")
                    continue
                else:
                    break
        except:
            continue;

    acc = Account(username, code, m)
    accounts.append(acc)
    mainMenu()

def main():
   mainMenu() 


if __name__ == "__main__":
    main()

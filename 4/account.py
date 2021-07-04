class Account:
    def __init__(self, name, code, m):
        self.username = name
        self.code = code
        self.m = m

    def AddMoney(self, summ):
        self.m.summ = self.m.summ + summ

    def SubMoney(self, summ):
        if self.m.summ < summ:
            return -1
        else:
            self.m.summ = self.m.summ - summ
            return 1

    def show(self):
        print(f"Имя пользователя: {self.username} Идентификационный код: {self.code}")

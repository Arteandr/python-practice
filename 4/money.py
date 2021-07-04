class Money:
    def __init__(self, currency, summ):
        self.currency = currency
        self.summ = summ

    def show(self):
        print(f"Название валюты: {self.currency} Сумма: {self.summ}")

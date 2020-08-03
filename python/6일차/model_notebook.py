class Notebook():
    def __init__(self, _BRAND, _NAME, _DATE, _RANK, _LOW_PRICE, _SELLER, _GPA):
        self.BRAND = _BRAND
        self.NAME = _NAME
        self.DATE = _DATE
        self.RANK = _RANK
        self.LOW_PRICE = _LOW_PRICE
        self.SELLER = _SELLER
        self.GPA = _GPA       

    def show(self):
        line = 'BRAND: {0}  NAME: {1}  DATE: {2}  RANK: {3}  LOW_PRICE: {4}'.format(self.BRAND, self.NAME, self.DATE, self.RANK, self.LOW_PRICE)
        print(line)
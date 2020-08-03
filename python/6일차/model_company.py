class Company:
    def __init__(self, _search, _brand, _date, _rank, _nation):
        self.search = _search
        self.brand = _brand
        self.date = _date
        self.rank = _rank
        self.nation = _nation

    def show(self):
        line = 'SEARCH: {0}  BRAND: {1}  DATE: {2}  RANK: {3}  NATION: {4}'.format(self.search, self.brand, self.date, self.rank, self.nation)
        print(line)

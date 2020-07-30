class Nation:
    def __init__(self, _num, _nation, _capital, _population):
        self.num = _num
        self.nation = _nation
        self.capital = _capital
        self.population = _population

    def SaveLine(self):
        line = '{0};{1};{2};{3}\n'.format(self.num, self.nation, self.capital, self.population)
        return line
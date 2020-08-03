class Pop_mall:
    def __init__(self, _rank, _date, _name):
        self.rank = _rank
        self.date = _date
        self.name = _name

    def show(self):
        line = 'RANK: {0}  DATE: {1}  NAME: {2}'.format(self.rank, self.date, self.name)
        print(line)
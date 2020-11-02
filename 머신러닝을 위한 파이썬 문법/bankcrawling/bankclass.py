class Bank:
    def __init__(self, _name, _exchange_rate, _save, _save_rate, _date):
        self.name = _name
        self.exchange_rate = _exchange_rate
        self.save = _save
        self.save_rate = _save_rate
        self.date = _date

    def show(self):
        exInfo = '{0} {1} {2} {3}'.format(self._name, self._exchange_rate, self._save, self._date)
        print(exInfo)
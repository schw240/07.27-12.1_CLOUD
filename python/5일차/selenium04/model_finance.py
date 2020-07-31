class Finance:
    def __init__(self, _code, _date, _open, _high, _low, _close, _adj_close, _volume):
        self.code = _code
        self.date = _date
        self.open = _open
        self.high = _high
        self.low = _low
        self.close = _close
        self.adj_close = _adj_close
        self.volume = _volume

    def show(self):
        line = '{0} {1} {2}'.format(self.code, self.date, self.high)
        print(line)
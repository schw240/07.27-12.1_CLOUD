class Staff:
    def __init__(self, _code, _k_name, _nation, _is_director):
        self.code = _code
        self.k_name = _k_name
        self.nation = _nation
        self.is_director = _is_director

    def show(self, count):
        line = '{0}  CODE:  {1}\t배우:  {2}'.format(count, self.code, self.k_name)
        print(line)
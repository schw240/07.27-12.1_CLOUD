class Movie:
    def __init__(self,  _title):
        self.title = _title
       

    def show(self, count):
        line = '{0}번째  영화 제목:  {1} '.format(count, self.title)
        print(line)
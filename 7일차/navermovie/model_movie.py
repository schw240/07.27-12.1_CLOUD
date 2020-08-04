class Movie:
    def __init__(self, _code, _title, _story, _genre, _rating, _run_time, _open_date):
        self.code = _code
        self.title = _title
        self.story = _story
        self.genre = _genre
        self.rating = _rating
        self.run_time = _run_time
        self.open_date = _open_date

    def show(self, count):
        line = '{0}    CODE:  {1}, 영화:  {2}'.format(count, self.code, self.title)
        print(line)

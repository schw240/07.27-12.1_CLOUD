class Dog:
    def __init__(self, _name, _kind, _age, _isNeut):
        self.name = _name
        self.kind = _kind
        self.age = _age
        self.isNeut = _isNeut

    def ShowProfile(self):
        print("이름: {0}\t견종: {1}\t나이: {2}\t중성화: {3}".format(self.name, self.kind, self.age, self.isNeut))

    def WriteLine(self):
        line = '{0};{1};{2};{3}\n'.format(self.name, self.kind, self.age, self.isNeut)
        return  line
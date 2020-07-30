class dogModel:

    def __init__(self, _name, _age, _kind, _no):
        self.name = _name
        self.age = _age
        self.kind = _kind
        self.no = _no


    def WriteLine(self): #클래스 안에있는 인스턴스이기 때문에 self를 넣어줘야함
        #print(self.name, self.armor, self.nation, self.age, self.ishero)
        return '{0};{1};{2};{3};{4}\n'.format(self.name, self.age, self.kind, self.no)

    def showProfile(self):
        print('이름: {0}  나이: {1}  견종: {2}  중성화: {3}'.format(self.name, self.age, self.kind, self.no))

    def upper(self):
        return self.upper()

    def lower(self):
        return self.lower()
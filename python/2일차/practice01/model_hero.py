class HeroModel:


    #생성자 메서드
    def __init__(self, _nation, _name, _age, _armor, _ishero):
        self.nation = _nation
        self.name = _name
        self.age = _age
        self.armor = _armor
        self.ishero = _ishero

    
    #클래스 안에다가 메서드를 만듬
    def ShowProfile(self): #클래스 안에있는 인스턴스이기 때문에 self를 넣어줘야함
        #print(self.name, self.armor, self.nation, self.age, self.ishero)
        print('국가: {0} 이름: {1}  ({2}) 주무기: {3} 현재 활동상태: {4}'.format(self.nation, self.name, self.age, self.armor, self.ishero))

    def WriteLine(self): #클래스 안에있는 인스턴스이기 때문에 self를 넣어줘야함
        #print(self.name, self.armor, self.nation, self.age, self.ishero)
        return '{0};{1};{2};{3};{4}\n'.format(self.nation, self.name, self.armor, self.age, self.ishero)

    def readLine(self):
        return 


    def upper(self):
        return self.name.upper()


    def lower(self):
        return self.nation.lower()
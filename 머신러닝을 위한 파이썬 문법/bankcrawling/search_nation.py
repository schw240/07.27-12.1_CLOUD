def search_nation():
    f = open('국가명.txt' , 'r')
    nations = list()
    nation = f.readline()
    nations = nation.split(',')
    print(nation)
    del nations[-1]
    print(nation)
    return nations
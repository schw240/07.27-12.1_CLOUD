from model_nation import Nation

f = open('c:/07.27-12.1_CLOUD/python/4일차/nat_list.txt', 'r', encoding='utf8')

nat_list = list()

for line in f.readlines():
    #split를 이용해 잘랐으므로 items는 리스트가 됨
    items = line.replace('\n', '').split(';')
    num = int(items[0])
    nation = items[1]
    capital = items[2]
    population = int(items[3])

    nat = Nation(num, nation, capital, population)
    nat_list.append(nat)

f.close

for n in nat_list:
    print(n.num, n.nation, n.capital, n.population)
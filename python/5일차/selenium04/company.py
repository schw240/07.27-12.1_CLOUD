from model_company import Company
import csv

company_list = list()

def LoadCompany():
    
    with open('C:/07.27-12.1_CLOUD/python/finance/companylist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            _symbol = row["Symbol"]
            _name = row["Name"]
            _last_sale = row["LastSale"]
            _market_cap = row["MarketCap"]
            _ipo_year = row["IPOyear"]
            _sector = row["Sector"]
            _industry = row["industry"]
            _summary_quote = row["Summary Quote"]

            comp = Company(_symbol, _name, _last_sale, _market_cap, _ipo_year, _sector, _industry, _summary_quote)
            company_list.append(comp)
    return company_list

comps = LoadCompany()

for comp in comps:
    print(comp.symbol, comp.name)
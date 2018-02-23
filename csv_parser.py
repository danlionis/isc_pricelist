import csv

index_pricelist_region = 0          # A
index_pricelist_country = 1         # B
index_pricelist_mcc = 3             # D
index_pricelist_mnc = 4             # E
index_pricelist_price = 5           # F

index_marketshare_region = 0        # A
index_marketshare_country = 1       # B
index_marketshare_operator = 2      # C
index_marketshare_mcc = 3           # D
index_marketshare_mnc = 4           # E
index_marketshare_marketshare = 5   # F

def parse_price(file_name):
    ps = []
    with open(file_name) as price_csv:
        columns = csv.reader(price_csv)

        # next(columns, None)

        for row in columns:
            mcc, mnc_list, price = process_pricelist_row(row)

            for mnc in mnc_list:
                ps.append({
                    'price': price,
                    'mcc': int(mcc),
                    'mnc': int(mnc)
                })

    return ps

def process_pricelist_row(row):
    mcc = row[index_pricelist_mcc]
    mnc_list_string = row[index_pricelist_mnc].split(',')
    price_string = row[index_pricelist_price].replace(',', '.')
    country = row[index_pricelist_country]

    # map mcc string to integer
    if mcc:
      mcc = int(mcc)

    # map mnc strings to integer
    mnc_list = [int(x) for x in mnc_list_string]

    # if mcc == 262:
    #   print(mcc, mnc_list)

    if not price_string:
        price = 0
    else:
        price = float(price_string)
    return mcc, mnc_list, price



def process_marketshare_row(row):
    mcc = row[index_marketshare_mcc]
    mnc = row[index_marketshare_mnc]

    if not mcc == "":
      mcc = int(mcc)
    if not mnc == "":
      mnc = int(mnc)

    # mcc = int(mcc)
    # mnc = int(mnc)

    # if mcc == 262:
    #   print(mcc, type(mcc), mnc, type(mnc))

    marketshare = row[index_marketshare_marketshare].replace('%', '').replace(',', '.')
    marketshare = float(marketshare) / 100

    country = row[index_marketshare_country]
    region = row[index_marketshare_region]
    operator = row[index_marketshare_operator]

    return region, country, operator, mcc, mnc, marketshare

def parse_marketshare(file_name):
    ms = []
    with open(file_name) as marketshares_csv:
        columns = csv.reader(marketshares_csv)

        for row in columns:
            region, country, operator, mcc, mnc, marketshare = process_marketshare_row(row)

            ms.append({
                'region': region,
                'country': country,
                'operator': operator,
                'mcc': mcc,
                'mnc': mnc,
                'marketshare': marketshare,
            })

    return ms

import csv
import normalize

index_pricelist_region = 0  # A
index_pricelist_country = 1  # B
index_pricelist_mcc = 3  # D
index_pricelist_mnc = 4  # E
index_pricelist_price = 5  # F

index_marketshare_region = 0  # A
index_marketshare_country = 1  # B
index_marketshare_operator = 2  # C
index_marketshare_mcc = 3  # D
index_marketshare_mnc = 4  # E
index_marketshare_marketshare = 5  # F


def parse_price(file_name):
    ps = []
    with open(file_name) as price_csv:
        columns = csv.reader(price_csv)

        # next(columns, None)

        for i, row in enumerate(columns):
            mcc, mnc_list, price = process_pricelist_row(row, i, file_name)

            for mnc in mnc_list:
                ps.append({
                    'price': price,
                    'mcc': mcc,
                    'mnc': mnc
                })

    return ps


def process_pricelist_row(row, row_index, table_name=""):
    mcc = row[index_pricelist_mcc]
    mnc_list = row[index_pricelist_mnc].split(',')
    price = row[index_pricelist_price]

    # normalize all rows throw exception if row not properly formatted
    mcc = normalize.normalize_mcc(mcc, row_index, table_name=table_name)
    mnc_list = [normalize.normalize_mnc(mnc, row_index, table_name=table_name) for mnc in mnc_list]
    price = normalize.normalize_price(price, row_index, table_name=table_name)

    return mcc, mnc_list, price


def process_marketshare_row(row, row_index, table_name=""):
    mcc = row[index_marketshare_mcc]
    mnc = row[index_marketshare_mnc]
    market_share = row[index_marketshare_marketshare].replace('%', '').replace(',', '.')

    mcc = normalize.normalize_mcc(mcc, row_index, table_name=table_name)
    mnc = normalize.normalize_mnc(mnc, row_index, table_name=table_name)
    market_share = normalize.normalize_market_share(market_share, row_index, table_name=table_name)

    country = row[index_marketshare_country]
    region = row[index_marketshare_region]
    operator = row[index_marketshare_operator]

    return region, country, operator, mcc, mnc, market_share


def parse_marketshare(file_name):
    ms = []
    with open(file_name) as marketshares_csv:
        columns = csv.reader(marketshares_csv)

        for i, row in enumerate(columns):
            region, country, operator, mcc, mnc, marketshare = process_marketshare_row(row, i, table_name=file_name)

            ms.append({
                'region': region,
                'country': country,
                'operator': operator,
                'mcc': mcc,
                'mnc': mnc,
                'marketshare': marketshare,
            })

    return ms

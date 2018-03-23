def normalize_price(price, row_index, table_name=""):
    price = price.replace(',', '.')
    if price:
        try:
            return float(price)
        except ValueError:
            print("Value Error at row {0} in {1}. price \"{2}\" is not a number!".format(row_index + 1, table_name, price))
    return 0


def normalize_mcc(mcc, row_index, table_name=""):
    if mcc:
        try:
            return int(mcc)
        except ValueError:
            print("Value Error at row {0} in {1}. mcc \"{2}\" is not a number".format(row_index + 1, table_name, mcc))
    return None


def normalize_mnc(mnc, row_index, table_name=""):
    if mnc:
        try:
            return int(mnc)
        except ValueError:
            print("Value Error at row {0} in {1}. mnc \"{2}\" is not a number".format(row_index + 1, table_name, mnc))
    return None


def normalize_market_share(market_share, row_index, table_name=""):
    if market_share:
        try:
            return float(market_share) / 100
        except ValueError:
            print("Value Error at row {0} in {1}. market share \"{2}\" is not a number".format(row_index + 1, table_name, mnc))

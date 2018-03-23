import csv
import itertools
import sys, getopt
from pprint import pprint
from operator import itemgetter
import copy

from csv_parser import parse_price, parse_marketshare

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'p:m:', ['pricelist=', 'marketshare='])
    except getopt.GetoptError:
        print('pricelist.py <pricelist.csv> <marketshare.csv>')
        sys.exit(2)

    if len(argv) < 2:
        filename_pricelist = './pricelist.csv'
        filename_marketshares = './marketshares.csv'
    else:
        filename_pricelist = args[0]
        filename_marketshares = args[1]

    start(filename_pricelist, filename_marketshares, 'out', 10)


def generate_pricelist(path_pricelist, path_marketshare, path_savefile, marge=10):
    start(path_pricelist, path_marketshare, path_savefile, marge)


def start(filename_pricelist, filename_marketshares, path_savefile, marge):
    # parse the prices from the pricelist table
    prices = parse_price(filename_pricelist)

    # parse the marketshares from the marketshare table
    marketshares = parse_marketshare(filename_marketshares)

    # combine prices with marketshares to calculate a weighted price
    weighted = calc_weighted(prices, marketshares)

    # write the weighted prices to a file
    write_weighted(weighted, path_savefile)

    # group and calculated a price for the country
    grouped = group_weighted(weighted, marge)

    # write the final prices to a table
    write_grouped(grouped, path_savefile)
    write_final(grouped, path_savefile)
    print("============== COMPLETE ==============")


def write_grouped(grouped, file_name):
    with open(file_name + "/cost_country.csv", 'w') as calculated:
        fieldnames = ['region', 'country', 'operator_count', 'cost','marketshare', 'marge', 'salesprice']
        writer = csv.DictWriter(calculated, fieldnames=fieldnames, extrasaction='ignore', lineterminator='\n')

        writer.writeheader()

        for group in grouped:
            writer.writerow(group)


def write_final(grouped, file_name):
    with open(file_name + '/salesprice.csv', 'w') as list:
        fieldnames = ['region', 'country', 'salesprice']
        writer = csv.DictWriter(list, fieldnames=fieldnames, extrasaction='ignore', lineterminator='\n')

        writer.writeheader()

        for group in grouped:
            writer.writerow(group)


def group_weighted(weighted, marge):
    sorted_prices = sorted(weighted, key=itemgetter('country'))

    grouped = []

    for key, operators in itertools.groupby(sorted_prices, key=itemgetter('country')):
        group = {'country': key, 'price': 0, 'marketshare': 0}

        # copy the object without references
        ops = copy.deepcopy(operators)
        operator_list = list(ops)

        marketshare_total = sum([x['marketshare'] for x in operators])
        marketshare_diff = 1 - marketshare_total

        group['marketshare'] = marketshare_total


        for op in operator_list:
          op['marketshare'] = op['marketshare'] / marketshare_total
          op['weighted_price']  = op['price'] * op['marketshare']

        for op in operator_list:
            group['price'] += op['weighted_price']
            group['region'] = op['region']

        group['operator_count'] = len(list(operator_list))
        group['cost'] = round(group['price'], 5)
        group['marge'] = "{0}%".format(marge)
        group['salesprice'] = round(group['price'] * (1 + (marge / 100)), 5)
        group['marketshare'] = str(group['marketshare'] * 100) + "%"

        grouped.append(group)
    return grouped


def calc_weighted(prices, marketshares):
    weighted_prices = []
    for ms in marketshares:
        for p in prices:
            if (ms['mcc'] == p['mcc']) and (ms['mnc'] == p['mnc']):
                wp = p['price'] * ms['marketshare']
                weighted_prices.append({
                    'region': ms['region'],
                    'country': ms['country'],
                    'operator': ms['operator'],
                    'mcc': p['mcc'],
                    'mnc': p['mnc'],
                    'price': p['price'],
                    'marketshare': ms['marketshare'],
                    'weighted_price': wp
                })
    return weighted_prices


def write_weighted(weighted, file_name):
    with open(file_name + "/cost_operator.csv", 'w') as calculated_list:
        fieldnames = ['region', 'country', 'operator', 'mcc', 'mnc', 'price', 'marketshare', 'weighted_price']
        writer = csv.DictWriter(calculated_list, fieldnames=fieldnames, extrasaction='ignore', lineterminator='\n')

        writer.writeheader()

        for price in weighted:
            writer.writerow(price)


if __name__ == "__main__":
    main(sys.argv[1:])

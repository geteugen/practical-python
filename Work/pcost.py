# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    total = 0.0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=2):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total += nshares * price
            except ValueError:
                print("Warning, non numeric value found on line ", rowno)
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)

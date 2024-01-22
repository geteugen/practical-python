# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, row))
            holding["shares"] = int(holding["shares"])
            holding["price"] = float(holding["price"])
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        change = prices[holding["name"]] - holding["price"]
        report.append((holding["name"], holding["shares"], f'${prices[holding["name"]]:.2f}', change))
    return report


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
headers = ("Name", "Shares", "Price", "Change")
headers_first_line = f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}"
headers_second_line = " ".join(["-" * 10] * 4)
print(headers_first_line)
print(headers_second_line)
report = make_report(portfolio, prices)
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")

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


def print_report(report):
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(" ".join(["-" * 10] * 4))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report(portfolio_filename="Data/portfolio.csv", prices_filename="Data/prices.csv")

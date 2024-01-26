# report.py
#
# Exercise 2.4
import sys
from fileparse import parse_csv
from stock import Stock


def read_portfolio(filename):
    with open(filename) as f:
        portdicts = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float])
    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
    return portfolio


def read_prices(filename):
    with open(filename) as f:
        price_tuples = parse_csv(f, types=[str, float], has_headers=False)
    return {p[0]: p[1] for p in price_tuples}


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        change = prices[stock.name] - stock.price
        report.append((stock.name, stock.shares, f"${prices[stock.name]:.2f}", change))
    return report


def print_report(report, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples
    """
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


def main(argv):
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfolio_filename=portfile, prices_filename=pricefile)


if __name__ == "__main__":
    main(sys.argv)

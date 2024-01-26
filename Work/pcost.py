# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio
from stock import Stock


def portfolio_cost(filename):
    total = 0.0
    portfolio = read_portfolio(filename)
    for stock in portfolio:
        total += stock.shares * stock.price
    return total


def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        filename = "Data/portfolio.csv"

    cost = portfolio_cost(filename)
    print("Total cost:", cost)


if __name__ == "__main__":
    main(sys.argv)

# report.py
import sys

from . import tableformat
from .fileparse import parse_csv
from .stock import Stock
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    """
    Read a stock portfolio file into a list of dictionaries with keys: name, shares, and price
    """
    with open(filename) as lines:
        port = Portfolio.from_csv(lines)
    return port


def read_prices(filename):
    with open(filename) as f:
        price_tuples = parse_csv(f, types=[str, float], has_headers=False)
    return {p[0]: p[1] for p in price_tuples}


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        change = prices[stock.name] - stock.price
        report.append((stock.name, stock.shares, prices[stock.name], change))
    return report


def print_report(report, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    portfile = argv[1]
    pricefile = argv[2]
    format = argv[3]
    portfolio_report(portfoliofile=portfile, pricefile=pricefile, fmt=format)


if __name__ == "__main__":
    # This file sets up basic configuration of the logging module.
    # Change settings here to adjust logging output as needed.
    import logging

    logging.basicConfig(
        filename="app.log",  # Name of the log file (omit to use stderr)
        filemode="w",  # File mode (use 'a' to append)
        level=logging.WARNING,  # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    )
    main(sys.argv)

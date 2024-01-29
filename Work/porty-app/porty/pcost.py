import sys
from .report import read_portfolio


def portfolio_cost(filename):
    """
    Computes the total cost (share * price) of a porfolio file
    """
    portfolio = read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        filename = "Data/portfolio.csv"

    cost = portfolio_cost(filename)
    print("Total cost:", cost)


if __name__ == "__main__":
    main(sys.argv)

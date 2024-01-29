class FormatError(Exception):
    pass


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format.
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Output portfolio data in HTML format."""

    def headings(self, headers):
        print("<tr><th>" + "</th><th>".join(headers) + "</th></tr>")

    def row(self, rowdata):
        print("<tr><td>" + "</td><td>".join(rowdata) + "</td></tr>")


def create_formatter(name):
    if name == "txt":
        formatter = TextTableFormatter()
    elif name == "csv":
        formatter = CSVTableFormatter()
    elif name == "html":
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format {name}")
    return formatter


def print_table(portfolio, attributes, formatter):
    formatter.headings(attributes)
    for stock in portfolio:
        cells = [str(getattr(stock, attr)) for attr in attributes]
        formatter.row(cells)

# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if has_headers == False and select:
        raise RuntimeError("Select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        indices = []

        if has_headers:
            # Read the file headers
            headers = next(rows)

            if select:
                headers = select
                indices = [headers.index(colname) for colname in select]

        records = []
        for rownum, row in enumerate(rows):
            if not row:  # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Type conversion
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rownum}: Couldn't convert {row}")
                        print(f"Row {rownum}: Reason {e}")
                    continue

            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
            else:
                # Make a tuple
                record = tuple(row)

            records.append(record)

    return records

import csv
import logging

log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:  # Skip rows with no data
            continue

        # Filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        # Type conversion
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records

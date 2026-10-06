"""
Sales Data Processing Application
Day 3 Lab - File Handling, CSV/JSON, Exceptions, Modules
"""
import csv
import json
import os
from datetime import datetime

INPUT_FILE = "sales.csv"
OUTPUT_FILE = os.path.join("reports", "sales_summary.json")
REQUIRED_COLUMNS = ["order_id", "date", "product", "quantity", "unit_price"]


class InvalidRowError(Exception):
    """Raised when a sales row cannot be used."""
    pass


def read_sales(filename):
    """Read the CSV and return a list of row dictionaries."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Sales file '{filename}' not found.")

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"CSV is missing columns: {missing}")
        return list(reader)


def clean_row(row):
    """Validate one row and return it with proper types, or raise InvalidRowError."""
    product = (row.get("product") or "").strip()
    if not product:
        raise InvalidRowError("product name is missing")

    qty_text = (row.get("quantity") or "").strip()
    price_text = (row.get("unit_price") or "").strip()
    if not qty_text or not price_text:
        raise InvalidRowError("quantity or unit_price is missing")

    try:
        quantity = int(qty_text)
        unit_price = float(price_text)
    except ValueError:
        raise InvalidRowError(f"non-numeric value (quantity='{qty_text}', price='{price_text}')")

    if quantity <= 0 or unit_price <= 0:
        raise InvalidRowError("quantity and price must be positive")

    try:
        date = datetime.strptime(row["date"].strip(), "%Y-%m-%d").date()
    except ValueError:
        raise InvalidRowError(f"date '{row['date']}' is not in YYYY-MM-DD format")

    return {
        "order_id": row["order_id"],
        "date": date.isoformat(),
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "amount": quantity * unit_price,
    }


def process(rows):
    """Clean every row, collect errors, and build the summary."""
    valid, errors = [], []
    for line_no, row in enumerate(rows, start=2):   # line 1 is the header
        try:
            valid.append(clean_row(row))
        except InvalidRowError as e:
            errors.append({"line": line_no, "order_id": row.get("order_id"), "reason": str(e)})

    sales_by_product = {}
    for r in valid:
        sales_by_product[r["product"]] = sales_by_product.get(r["product"], 0) + r["amount"]

    if not sales_by_product:
        raise ValueError("No valid sales rows to summarise.")

    top_product = max(sales_by_product, key=sales_by_product.get)
    total_sales = sum(sales_by_product.values())

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_file": INPUT_FILE,
        "rows_read": len(rows),
        "valid_rows": len(valid),
        "invalid_rows": len(errors),
        "total_sales": round(total_sales, 2),
        "highest_selling_product": {
            "name": top_product,
            "sales": round(sales_by_product[top_product], 2),
        },
        "sales_by_product": {p: round(v, 2) for p, v in
                             sorted(sales_by_product.items(), key=lambda kv: kv[1], reverse=True)},
        "errors": errors,
    }


def export_summary(summary, filename):
    """Write the summary dictionary to a JSON file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)


def main():
    try:
        rows = read_sales(INPUT_FILE)
        summary = process(rows)
        export_summary(summary, OUTPUT_FILE)
    except FileNotFoundError as e:
        print("ERROR:", e)
        print("Tip: check the file name and that you are in the right folder.")
    except ValueError as e:
        print("ERROR:", e)
    except PermissionError:
        print(f"ERROR: cannot write '{OUTPUT_FILE}'. Is it open in another program?")
    else:
        print(f"Rows read      : {summary['rows_read']}")
        print(f"Valid rows     : {summary['valid_rows']}")
        print(f"Invalid rows   : {summary['invalid_rows']}")
        for err in summary["errors"]:
            print(f"   - line {err['line']} (order {err['order_id']}): {err['reason']}")
        print(f"Total sales    : Rs. {summary['total_sales']:,.2f}")
        top = summary["highest_selling_product"]
        print(f"Top product    : {top['name']} (Rs. {top['sales']:,.2f})")
        print(f"Summary saved  : {OUTPUT_FILE}")
    finally:
        print("Sales processing finished.")


if __name__ == "__main__":
    main()

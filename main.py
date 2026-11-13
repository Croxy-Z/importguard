import csv

with open("products.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    if reader.fieldnames is None:
        print("CSV file is empty")
    else:
        column_names = reader.fieldnames
        required_fields = {"sku", "name", "price", "quantity"}
        missing_fields = required_fields.difference(column_names)

        if not missing_fields:
            for index, line in enumerate(reader, start=2):
                print(f"Row: {index}. {line}")
        else:
            print(f"Missing fields: {missing_fields}")
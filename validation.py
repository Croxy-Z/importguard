def validate_product(product):
    errors = []
    required_fields = ["sku", "name", "price", "quantity"]

    for field in required_fields:
        if field not in product:
            errors.append(f"Field {field} is missing")
        elif field in ("sku", "name"):
            try:
                if not product[field].strip():
                    errors.append(f"Field {field} is empty")
            except AttributeError:
                errors.append(f"Field {field} value is incorrect: {product[field]}")
        elif field == "price":
            try:
                price = float(product[field])
            except (ValueError, TypeError):
                errors.append(f"Field {field} value is incorrect: {product[field]}")
            else:
                if price <= 0:
                    errors.append(f"Price must be greater than 0: {product[field]}")
        elif field == "quantity":
            try:
                quantity = int(product[field])
            except (ValueError, TypeError):
                errors.append(f"Field {field} value is incorrect")
            else:
                if quantity < 0:
                    errors.append(f"Quantity cannot be negative: {product[field]}")

    if not errors:
        validated_product = {
            "sku": product["sku"],
            "name": product["name"],
            "price": price,
            "quantity": quantity
        }

        return errors, validated_product

    return errors, None

def validate_catalog(catalog):
    catalog_errors = []
    seen_skus = set()
    validated_products = []

    for index, product in enumerate(catalog, start=1):
        product_errors, validated_product = validate_product(product)

        if "sku" in product and product["sku"].strip():
            if product["sku"] not in seen_skus:
                seen_skus.add(product["sku"])
            else:
                product_errors.append(f"Sku {product['sku']} already exists")

        if product_errors:
            for error in product_errors:
                catalog_errors.append(f"Product: {index}: {error}")
        elif not catalog_errors:
            validated_products.append(validated_product)

    if catalog_errors:
        return catalog_errors, []

    return [], validated_products
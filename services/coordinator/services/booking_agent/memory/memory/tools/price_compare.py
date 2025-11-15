def compare_prices(options: list):
    # Sort options by available price field
    return sorted(options, key=lambda o: o.get("price") or o.get("price_per_night") or 1e9)

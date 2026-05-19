def explain_transaction(text):
    flags = []
    t = text.lower()

    # High amount
    if any(x in t for x in ["50000", "70000", "90000", "100000"]):
        flags.append("High transaction amount")

    # Foreign location
    if any(x in t for x in ["usa", "russia", "china", "uk"]):
        flags.append("Foreign transaction")

    # Odd time
    if any(x in t for x in ["01:", "02:", "03:", "04:"]):
        flags.append("Odd hour transaction")

    # ATM usage unusual
    if "atm" in t and "different location" in t:
        flags.append("Unusual ATM usage")

    return flags
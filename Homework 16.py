def compute_change(bill_amount, paid_amount, denominations=None):
    """
    bill_amount and paid_amount as floats or decimals (dollars).
    Returns (change_total, breakdown) where breakdown is list of (denom, count).
    """
    if paid_amount < bill_amount:
        raise ValueError("Paid amount is less than bill amount.")
    if denominations is None:
        denominations = [10000, 5000, 2000, 1000, 500, 100, 50, 25, 10, 5, 1]
        names = ["$100", "$50", "$20", "$10", "$5", "$1", "50¢", "25¢", "10¢", "5¢", "1¢"]
    else:
        names = [str(d) for d in denominations]

    # convert to cents to avoid float issues
    bill_cents = round(bill_amount * 100)
    paid_cents = round(paid_amount * 100)
    change_cents = paid_cents - bill_cents

    breakdown = []
    remaining = change_cents
    for denom, name in zip(denominations, names):
        count = remaining // denom
        if count:
            breakdown.append((name, int(count)))
            remaining -= denom * count

    return change_cents / 100.0, breakdown

# Example 
def main():
    try:
        bill = float(input("Enter bill amount (e.g., 13.75): ").strip())
        paid = float(input("Enter paid amount (e.g., 20.00): ").strip())
        change, breakdown = compute_change(bill, paid)
        print(f"Total change: ${change:.2f}")
        if breakdown:
            print("Change given as:")
            for name, count in breakdown:
                print(f"  {count} x {name}")
        else:
            print("No change needed.")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

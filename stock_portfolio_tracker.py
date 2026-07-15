import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 145,
    "TSLA": 250,
    "META": 300,
    "NFLX": 450,
    "NVDA": 900,
}


def display_available_stocks():
    print("\nAvailable stocks and prices:")
    print("-" * 30)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<10} ${price}")
    print("-" * 30)


def get_portfolio_input():
    """Collects stock name + quantity pairs from the user until they type 'done'."""
    portfolio = {}
    display_available_stocks()
    print("\nEnter stock name and quantity (type 'done' when finished)\n")

    while True:
        stock_name = input("Stock name: ").strip().upper()
        if stock_name == "DONE":
            break

        if stock_name not in STOCK_PRICES:
            print(f"  '{stock_name}' not found in price list. Try again.\n")
            continue

        qty_input = input(f"Quantity of {stock_name}: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("  Quantity must be a positive whole number.\n")
                continue
        except ValueError:
            print("  Please enter a valid whole number.\n")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"  Added {quantity} share(s) of {stock_name}.\n")

    return portfolio


def calculate_investment(portfolio):
    """Returns a per-stock breakdown and the grand total investment value."""
    breakdown = []
    total = 0
    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        total += value
        breakdown.append((stock, quantity, price, value))
    return breakdown, total


def display_summary(breakdown, total):
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    print("-" * 45)
    for stock, quantity, price, value in breakdown:
        print(f"{stock:<8}{quantity:<6}${price:<9}${value:,.2f}")
    print("-" * 45)
    print(f"TOTAL INVESTMENT VALUE: ${total:,.2f}")
    print("=" * 45)


def save_to_file(breakdown, total):
    """Optionally saves the summary to a .txt or .csv file."""
    choice = input("\nSave results to a file? (y/n): ").strip().lower()
    if choice != "y":
        return

    file_format = input("Format - txt or csv? ").strip().lower()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if file_format == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, quantity, price, value in breakdown:
                writer.writerow([stock, quantity, price, f"{value:.2f}"])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", f"{total:.2f}"])
    else:
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}\n")
            f.write("-" * 45 + "\n")
            for stock, quantity, price, value in breakdown:
                f.write(f"{stock:<8}{quantity:<6}${price:<9}${value:,.2f}\n")
            f.write("-" * 45 + "\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total:,.2f}\n")

    print(f"Saved to {filename}")


def main():
    print("=" * 45)
    print("      STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)
    display_summary(breakdown, total)
    save_to_file(breakdown, total)


if __name__ == "__main__":
    main()

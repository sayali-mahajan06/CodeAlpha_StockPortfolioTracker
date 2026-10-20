stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n=== Portfolio Summary ===")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value

    print(
        f"{stock}: {quantity} shares × "
        f"${stock_prices[stock]} = ${value}"
    )

print("\nTotal Investment: $", total_investment)
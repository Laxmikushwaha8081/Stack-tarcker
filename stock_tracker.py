
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 190
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks:")

for stock in stock_prices:
    print(stock, "- Price: $", stock_prices[stock])

# Number of different stocks
n = int(input("\nHow many stocks do you want to buy? "))

# Store portfolio details
portfolio = []

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            investment = stock_prices[stock] * quantity
            total_investment += investment

            portfolio.append(
                [stock, quantity, stock_prices[stock], investment]
            )

            print("Investment value: $", investment)
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Stock not available!")

# Display final portfolio
print("\n===== YOUR PORTFOLIO =====")

for item in portfolio:
    print(item[0], "| Quantity:", item[1],
          "| Price: $", item[2],
          "| Total: $", item[3])

print("\nTotal Investment: $", total_investment)

# Save results to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n")

    for item in portfolio:
        file.write(
            item[0] + " | Quantity: " + str(item[1]) +
            " | Price: $" + str(item[2]) +
            " | Total: $" + str(item[3]) + "\n"
        )

    file.write("\nTotal Investment: $" + str(total_investment))

print("\nPortfolio saved to portfolio.txt")
# Stack-tarcker

A simple Python-based stock portfolio tracker that calculates total investment using predefined stock prices and user-entered quantities, with an option to save portfolio details to a text file.

## Project Overview

This project is a beginner-friendly command-line application built in Python. It allows a user to:

- view available stocks and their current prices
- enter stock symbols and quantities
- validate stock availability and quantity inputs
- calculate the total investment for each purchase
- track the overall portfolio value
- save the final portfolio details to a text file

## Features

- Predefined stock list with sample prices
- Multi-stock portfolio tracking
- Input validation for invalid symbols and non-positive quantities
- Console-based interface
- Output saved to `portfolio.txt`

## Supported Stocks

The program currently includes these stocks:

- AAPL - $180
- TSLA - $250
- GOOGL - $150
- MSFT - $400
- AMZN - $190

## Project Structure

```text
Stock tracker/
├── stock_tracker.py
├── portfolio.txt
├── README.md
```

## Requirements

- Python 3.x
- No external libraries required

## How to Run

Open a terminal in the project folder and run:

```bash
python stock_tracker.py
```

## How It Works

1. The program displays the list of available stocks and their prices.
2. The user enters how many stock entries they want to add.
3. For each stock, the user provides:
   - stock symbol
   - quantity
4. The program checks whether the stock exists and whether the quantity is greater than zero.
5. It calculates the investment total for each stock and the overall portfolio total.
6. It prints the portfolio summary and saves it to `portfolio.txt`.

## Example Output

```text
===== STOCK PORTFOLIO TRACKER =====

Available Stocks:
AAPL - Price: $ 180
TSLA - Price: $ 250
GOOGL - Price: $ 150
MSFT - Price: $ 400
AMZN - Price: $ 190

===== YOUR PORTFOLIO =====
AAPL | Quantity: 2 | Price: $ 180 | Total: $ 360

Total Investment: $ 360

Portfolio saved to portfolio.txt
```

## Notes

- This is a simple portfolio calculator designed for learning and demonstration purposes.
- Stock prices are predefined and static, not connected to live market data.
- The generated `portfolio.txt` file stores the final portfolio report.

## License

This project is provided for educational use.


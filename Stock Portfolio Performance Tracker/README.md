# 📈 Investment Portfolio Tracker

## Project Overview

The **Investment Portfolio Tracker** is a Python-based utility that helps users track their stock investments and monitor portfolio performance.

Users can enter stock ticker symbols, purchase prices, and share quantities. The program calculates the total invested capital, current market value, and percentage gain or loss for each stock holding.

It also exports portfolio transaction summaries into a CSV file for future reference and analysis.

## ✨ Features

- **Stock Symbol Validation:** Validates ticker symbols using an S&P 500 dataset.
- **Portfolio Management:** Stores stock holdings using Python dictionaries.
- **Price Lookup:** Supports optional recent stock-price retrieval using Yahoo Finance (`yfinance`).
- **Manual Price Entry:** Allows users to enter current stock prices manually.
- **Investment Calculations:** Calculates invested capital, market value, and gain/loss.
- **Performance Tracking:** Calculates individual and overall portfolio returns.
- **CSV Export:** Automatically saves portfolio summaries into a CSV file.
- **Formatted Console Output:** Displays portfolio performance in a structured table.

## 🛠️ Technologies Used

- Python 3
- CSV Module
- File Handling
- Dictionaries
- Exception Handling
- yfinance (optional)

## 📁 Project Structure

```text
Stock Portfolio Performance Tracker/
│
├── constituents.csv
├── portfolio.py
├── portfolio_summary.csv
└── README.md
```

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3 from:

https://www.python.org/downloads/

Verify the installation:

```bash
py --version
```

### 2. Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd "Stock Portfolio Performance Tracker"
```

### 3. Install Optional Dependency

To enable recent stock-price lookup, install:

```bash
py -m pip install yfinance
```

The program also works without this package by using manual price entry.

## ▶️ How to Run

Execute the following command in the terminal:

```bash
py portfolio.py
```

### User Input Example

```text
Enter stock ticker (or DONE to finish): AAPL

Enter purchase price for AAPL ($): 180

Enter number of shares for AAPL: 10

Fetch a recent price for AAPL using yfinance? (y/n): n

Enter current price for AAPL ($): 200
```

To finish entering stocks:

```text
Enter stock ticker (or DONE to finish): DONE
```

## 🧮 Calculation Method

The program uses the following formulas:

**1. Invested Capital**

```text
Invested Capital = Purchase Price × Number of Shares
```

**2. Current Market Value**

```text
Market Value = Current Price × Number of Shares
```

**3. Gain or Loss**

```text
Gain/Loss = Market Value - Invested Capital
```

**4. Percentage Gain or Loss**

```text
Return (%) = (Gain/Loss / Invested Capital) × 100
```

## 📊 Sample Output

```text
PORTFOLIO SUMMARY

Ticker    Shares   Buy Price   Current   Market Value   Gain/Loss   Return
AAPL         10     $180.00    $200.00     $2,000.00      $200.00    11.11%

Total invested : $1,800.00
Current value  : $2,000.00
Total gain/loss: $200.00
Overall return : 11.11%

CSV report saved to: portfolio_summary.csv
Portfolio tracking completed.
```

*Note: The above values are illustrative examples.*

## 📄 CSV Export

After the user finishes entering stock holdings, the application generates:

`portfolio_summary.csv`

The file contains:

- Timestamp
- Stock ticker
- Company name
- Number of shares
- Purchase price
- Current price
- Invested capital
- Market value
- Gain or loss
- Gain or loss percentage

The application appends new portfolio summaries to the CSV file instead of overwriting previous records.

## 🚀 Future Enhancements

- Support multiple purchases of the same stock.
- Add a graphical user interface.
- Generate portfolio performance charts.
- Add historical stock-price analysis.
- Support additional stock exchanges.
- Introduce portfolio risk analysis.

## ⚠️ Disclaimer

This project is developed for educational purposes. Stock prices obtained through external services may be delayed or unavailable. The application is a portfolio tracking utility and does not provide financial or investment advice.

## 👩‍💻 Author

**Swamidas Bharathi**

GitHub: [sbharathi09](https://github.com/sbharathi09)

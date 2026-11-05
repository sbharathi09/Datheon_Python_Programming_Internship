
import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
TICKER_FILE = BASE_DIR / "constituents.csv"
OUTPUT_FILE = BASE_DIR / "portfolio_summary.csv"


def load_tickers():
    tickers = {}

    if not TICKER_FILE.exists():
        print("Warning: constituents.csv not found.")
        print("Ticker validation will be skipped.")
        return tickers

    with open(TICKER_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            symbol = (row.get("Symbol") or "").strip().upper()
            company = (row.get("Security") or "").strip()

            if symbol:
                tickers[symbol] = company or symbol

    return tickers


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a whole number greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_current_price(symbol):
    choice = input(
        f"Fetch a recent price for {symbol} using yfinance? (y/n): "
    ).strip().lower()

    if choice == "y":
        try:
            import yfinance as yf

            history = yf.Ticker(symbol).history(period="5d")
            closes = history["Close"].dropna()

            if not closes.empty:
                price = float(closes.iloc[-1])
                print(f"Recent closing price: ${price:.2f}")

                if input("Use this price? (y/n): ").lower() == "y":
                    return price

        except Exception:
            print("Live lookup failed. Enter the price manually.")

    return get_positive_float(
        f"Enter current price for {symbol} ($): "
    )


def save_summary(rows):
    columns = [
        "timestamp", "ticker", "company", "shares",
        "buy_price", "current_price", "invested_capital",
        "market_value", "gain_loss", "gain_loss_percent"
    ]

    file_exists = (
        OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0
    )

    timestamp = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)

        if not file_exists:
            writer.writeheader()

        for item in rows:
            record = {"timestamp": timestamp}

            for key in columns:
                if key == "timestamp":
                    continue

                value = item[key]

                if key in (
                    "buy_price", "current_price", "invested_capital",
                    "market_value", "gain_loss", "gain_loss_percent"
                ):
                    value = f"{value:.2f}"

                record[key] = value

            writer.writerow(record)


def main():
    print("=" * 65)
    print("          INVESTMENT PORTFOLIO TRACKER")
    print("=" * 65)

    ticker_map = load_tickers()

    if ticker_map:
        print(f"Loaded {len(ticker_map)} stock symbols.")

    portfolio = {}

    while True:
        symbol = input(
            "\nEnter stock ticker (or DONE to finish): "
        ).strip().upper()

        if symbol == "DONE":
            break

        if not symbol:
            print("Ticker cannot be empty.")
            continue

        if ticker_map and symbol not in ticker_map:
            print("Ticker not found in the S&P 500 dataset.")
            continue

        company = ticker_map.get(symbol, symbol)

        buy_price = get_positive_float(
            f"Enter purchase price for {symbol} ($): "
        )

        shares = get_positive_int(
            f"Enter number of shares for {symbol}: "
        )

        current_price = get_current_price(symbol)

       
        invested = buy_price * shares
        market_value = current_price * shares
        gain_loss = market_value - invested
        gain_percent = (gain_loss / invested) * 100

        portfolio[symbol] = {
            "ticker": symbol,
            "company": company,
            "shares": shares,
            "buy_price": buy_price,
            "current_price": current_price,
            "invested_capital": invested,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "gain_loss_percent": gain_percent,
        }

        print(f"Added {symbol} successfully.")

    if not portfolio:
        print("No holdings entered.")
        return

    rows = list(portfolio.values())

    total_invested = sum(
        item["invested_capital"] for item in rows
    )
    total_value = sum(
        item["market_value"] for item in rows
    )
    total_gain = total_value - total_invested
    total_return = (total_gain / total_invested) * 100

    print("\n" + "=" * 100)
    print("PORTFOLIO SUMMARY")
    print("=" * 100)

    print(
        f'{"Ticker":<9} {"Shares":>7} {"Buy Price":>12} '
        f'{"Current":>12} {"Market Value":>15} '
        f'{"Gain/Loss":>13} {"Return":>10}'
    )

    print("-" * 100)

    for item in rows:
        print(
            f'{item["ticker"]:<9} '
            f'{item["shares"]:>7} '
            f'${item["buy_price"]:>10,.2f} '
            f'${item["current_price"]:>10,.2f} '
            f'${item["market_value"]:>13,.2f} '
            f'${item["gain_loss"]:>11,.2f} '
            f'{item["gain_loss_percent"]:>8.2f}%'
        )

    print("-" * 100)
    print(f"Total invested : ${total_invested:,.2f}")
    print(f"Current value  : ${total_value:,.2f}")
    print(f"Total gain/loss: ${total_gain:,.2f}")
    print(f"Overall return : {total_return:.2f}%")

    save_summary(rows)

    print(f"\nCSV report saved to: {OUTPUT_FILE}")
    print("Portfolio tracking completed.")


if __name__ == "__main__":
    main()

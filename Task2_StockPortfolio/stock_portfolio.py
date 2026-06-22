stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

while True:
    stock = input("\nEnter stock symbol (or 'exit' to quit): ").upper()

    if stock == "EXIT":
        print("👋 Exiting program...")
        break

    if stock in stock_prices:
        print("✅ Stock is available!")

        # ✅ Inner loop: re-prompt until valid quantity is entered
        while True:
            quantity = input("Enter quantity: ")
            try:
                quantity = int(quantity)
                if quantity > 0:
                    break                      # valid — exit inner loop
                else:
                    print("❌ Quantity must be positive.")
            except ValueError:
                print("❌ Invalid input! Enter a whole number.")

        total = stock_prices[stock] * quantity

        print(f"\n📊 INVESTMENT SUMMARY")
        print(f"Stock:            {stock}")
        print(f"Price per share:  ${stock_prices[stock]}")
        print(f"Quantity:         {quantity} shares")
        print(f"Total Investment: ${total}")

        with open("portfolio.txt", "a") as f:
            f.write(f"Stock: {stock}\n")
            f.write(f"Price per share: ${stock_prices[stock]}\n")
            f.write(f"Quantity: {quantity} shares\n")
            f.write(f"Total Investment: ${total}\n")
            f.write("-" * 30 + "\n")          # ✅ separator between entries

        print("💾 Saved to portfolio.txt!")

    else:
        # ✅ Show available symbols on invalid stock
        print(f"❌ Stock not available! Try: {', '.join(stock_prices.keys())}")
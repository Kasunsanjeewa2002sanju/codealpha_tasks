def stock_portfolio_tracker():
    # Hardcoded dictionary of stock prices (stock symbol: price per share)
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "MSFT": 300.20,
        "AMZN": 120.90,
        "GOOGL": 135.60
    }
    
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    portfolio = {}
    total_value = 0.0
    
    while True:
        print("\nMenu:")
        print("1. Add stock to portfolio")
        print("2. View portfolio")
        print("3. Calculate total investment")
        print("4. Save portfolio to file")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Add stock to portfolio
            stock_symbol = input("Enter stock symbol: ").upper()
            
            if stock_symbol not in stock_prices:
                print("Error: Stock not found in our database.")
                continue
            
            try:
                quantity = int(input(f"Enter quantity of {stock_symbol}: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                
                portfolio[stock_symbol] = portfolio.get(stock_symbol, 0) + quantity
                print(f"Added {quantity} shares of {stock_symbol} to your portfolio.")
                
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")
        
        elif choice == "2":
            # View current portfolio
            if not portfolio:
                print("Your portfolio is empty.")
            else:
                print("\nYour Portfolio:")
                for stock, qty in portfolio.items():
                    print(f"{stock}: {qty} shares")
        
        elif choice == "3":
            # Calculate total investment
            if not portfolio:
                print("Your portfolio is empty.")
                continue
            
            total_value = 0.0
            print("\nInvestment Breakdown:")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                total_value += value
                print(f"{stock}: {qty} shares × ${stock_prices[stock]:.2f} = ${value:.2f}")
            
            print(f"\nTotal Investment Value: ${total_value:.2f}")
        
        elif choice == "4":
            # Save portfolio to file
            if not portfolio:
                print("Cannot save - portfolio is empty.")
                continue
            
            filename = input("Enter filename to save (e.g., portfolio.txt): ")
            try:
                with open(filename, 'w') as file:
                    file.write("Stock Portfolio\n")
                    file.write("===============\n")
                    for stock, qty in portfolio.items():
                        value = qty * stock_prices[stock]
                        file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]:.2f} = ${value:.2f}\n")
                    file.write(f"\nTotal Value: ${total_value:.2f}\n")
                print(f"Portfolio saved to {filename}")
            except IOError:
                print("Error saving file.")
        
        elif choice == "5":
            # Exit program
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the program
if __name__ == "__main__":
    stock_portfolio_tracker()
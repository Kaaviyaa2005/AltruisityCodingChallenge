def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

n = int(input("Enter the number of days: "))
prices = [int(input(f"Enter price for day {i + 1}: ")) for i in range(n)]
result = max_profit(prices)
print(result)
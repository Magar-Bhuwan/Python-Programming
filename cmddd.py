
current_price = float(input("Enter your current price: "))
target_price = float(input("Enter your target price: "))
daily_increase_rate = float(input("Enter your daily increase percentage: "))
rate = daily_increase_rate / 100
print("\n")

days = 0
starting_price = current_price

while current_price <= target_price:
    current_price *= (1 + rate)
    days += 1

print(f"Current price: Rs.{starting_price:,.2f}")        # i want to put the user entered current price here
print(f"Target price: Rs.{target_price:,.2f}")
print(f"Daily increase: {daily_increase_rate}%")
print(f"Days to reach target price: {days} days")
print(f"Final price after {days} days: Rs.{current_price:,.2f}")
print(f"After 7% cut off you will get total: {current_price -(current_price*0.07):,.2f}")

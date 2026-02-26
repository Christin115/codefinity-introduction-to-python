prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = .1
for cost in range(len(prices)):
    if cost == 0:
        discount_factor = .1
    elif cost == 1:
        discount_factor = .2
    elif cost == 2:
        discount_factor = .15
    elif cost == 3:
        discount_factor = .05
        
    prices[cost] -= prices[cost] * discount_factor
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")

    
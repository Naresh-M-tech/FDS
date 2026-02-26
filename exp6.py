# Item prices and quantities
prices = [100, 200, 150]
quantities = [2, 1, 3]

discount_rate = 10   # 10%
tax_rate = 5         # 5%

# Calculate subtotal
subtotal = sum(p*q for p, q in zip(prices, quantities))

# Apply discount
discount = subtotal * (discount_rate / 100)
after_discount = subtotal - discount

# Apply tax
tax = after_discount * (tax_rate / 100)
total_cost = after_discount + tax

print("Total Cost:", total_cost)

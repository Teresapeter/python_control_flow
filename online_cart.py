# Shopping cart used as dictionary
shopping_cart = {
    'shirt': 200,
    'trouser': 300,
    'skirt': 100,
}

# Calculating total cost of all items in the cart
total_cost = sum(shopping_cart.values())

# Apply discount of 10% if the total cost is above 150
if total_cost > 150:
    total_cost *= 0.9

# Check if the total cost is eligible for free shipping
if total_cost > 150:
    shipping_cost = 20
else:
    shipping_cost = 0

# Calculate the final total cost including shipping
final_total_cost = total_cost + shipping_cost

# Display the results
print("Total cost of items:", total_cost)
print("Shipping cost:", shipping_cost)
print("Ftotal cost:", final_total_cost)
menu = {
    "Burger": 50.00,
    "Fries": 30.00,
    "Soda": 25.00,
}

order = []

print("MENU")
for number, (product, price) in enumerate(menu.items(), start=1):
    print(f"{number}. {product} - P{price:.2f}")

while True:
    choice = input("Select a product number (or enter 0 to finish): ").strip()

    if choice == "0":
        break

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(menu):
        print("Invalid product number. Please try again.")
        continue

    product_names = list(menu.keys())
    product = product_names[int(choice) - 1]

    quantity_text = input(f"Enter quantity for {product}: ").strip()
    if not quantity_text.isdigit() or int(quantity_text) <= 0:
        print("Quantity must be a positive whole number.")
        continue

    quantity = int(quantity_text)
    subtotal = menu[product] * quantity
    order.append((product, quantity, menu[product], subtotal))
    print(f"Added {quantity} x {product}. Subtotal: P{subtotal:.2f}")

print("\nORDER SUMMARY")
total = 0.0
for product, quantity, price, subtotal in order:
    print(f"{product} x {quantity} @ P{price:.2f} = P{subtotal:.2f}")
    total += subtotal

print(f"Total: P{total:.2f}")

if order:
    while True:
        payment_text = input("Enter payment amount: ").strip()
        try:
            payment = float(payment_text)
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if payment < total:
            print("Payment is not enough.")
            continue

        change = payment - total
        print(f"Change: P{change:.2f}")
        break

def display_receipt(items):
	"""Print ordered items and return the total order amount.

	Each item is a dictionary containing ``name``, ``quantity``, and
	``price`` (the unit price).
	"""
	total = 0.0
	print("AINIKA SARI-SARI STORE")
	print("Receipt")

	for item in items:
		name = str(item["name"])
		quantity = item["quantity"]
		price = float(item["price"])
		amount = quantity * price
		total += amount
		print(f"{name} x{quantity} @ ${price:.2f} = ${amount:.2f}")

	print(f"Total: ${total:.2f}")
	return total

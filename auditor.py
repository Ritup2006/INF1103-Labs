# Requirement 1: Initialize the inventory to zero in the start
total_units = 0
failed_entries = 0

# Requirement 2: Run in a continuous loop until user types 'quit'
while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        break

    # Requirement 4: Input validation using .isdigit()
    if not user_input.isdigit():
        print("Error: Invalid entry. Please enter a positive whole number.")
        failed_entries += 1
        continue

    # Requirement 3: Accept stock values as integers
    quantity = int(user_input)

    # Requirement 5: Enforce business rules (reject negative numbers)
    if quantity < 0:
        print("Error: Negative values are not allowed.")
        failed_entries += 1
        continue

    # Requirement 6: Manage State (keep running total)
    total_units += quantity

    # Requirement 7: Trigger Overstock Alert (> 500 units)
    if total_units > 500:
        print("ALERT: Storage capacity exceeded (> 500 units)! Stopping audit.")
        break

# Requirement 8: Reporting summary
print("\n--- Audit Summary ---")
print(f"Total Units Processed: {total_units}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
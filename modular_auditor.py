def get_valid_input():
    stock_quantity = input("Enter Stock Quantity (Type 'quit' to quit): ")

    if stock_quantity.lower() == "quit": 
        return "quit"

    if not stock_quantity.isdigit():
        print("This number is rejected.")
        return None

    stock_actual = int(stock_quantity)

    if stock_actual < 0:
        print("Negative number rejected")
        return None
    
    return stock_actual


def process_delivery(current_total, new_value):
    new_total= current_total + new_value

    return new_total

def calculate_tax(amount):
    return amount*0.10

def generate_report(total_units, failed_attempts, deliveries_processed):
    print("Total Units:", total_units) 
    print("Total Deliveries Processed:", deliveries_processed) 
    print("Number of Failed/Rejected Entries:", failed_attempts)
















# inventory = 0
# failed_inventory = 0 

# while True: 
#     stock_quantity = input("Enter Stock Quantity (Type 'quit' to quit): ")
    
#     if stock_quantity.lower() == "quit": 
#         print("Total Units:", inventory)
#         break
        
  
#     if not stock_quantity.isdigit():
#         print("This number is rejected.")
#         failed_inventory += 1
#         continue
        
#     stock_actual = int(stock_quantity)
    

#     if stock_actual < 0:
#         print("Negative number rejected")
#         failed_inventory += 1
#         continue

#     inventory += stock_actual

#     if inventory > 500:
#         print("Alert, overloaded")
#         inventory -= stock_actual
#         break

# print("Total Units: ", inventory)
# print("Number of Failed inventory: ", failed_inventory)


# if __name__ == "__main__":
#     print(calculate_tax(100))



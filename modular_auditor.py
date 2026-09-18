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




def main():
    total_units = 0
    failed_entries = 0
    deliveries_processed = 0

    while True:
        user_input= get_valid_input()

        if user_input == "quit":
            break

        if user_input is None:
            failed_entries += 1
            continue

        total_units = process_delivery(total_units, user_input)
        deliveries_processed += 1
        total_tax = calculate_tax(total_units)

        print("total tax: ", total_tax)

        if total_units > 500:
            print("ALERT: Storage capacity exceeded (> 500 units)!")
            break

    # generate_report(total_units, failed_entries, deliveries_processed)






        

    # while True:
    #     user_input = get_valid_input()

    #     if user_input == "quit":
    #         break

    #     if user_input is None:
    #         failed_entries += 1
    #         continue

    #     total_units = process_delivery(total_units, user_input)
    #     deliveries_processed += 1

    #     if total_units > 500:
    #         print("ALERT: Storage capacity exceeded (> 500 units)! Stopping audit.")
    #         break

    # generate_report(total_units, failed_entries, deliveries_processed)
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


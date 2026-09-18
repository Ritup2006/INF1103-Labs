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


if __name__ == "__main__":
    print(process_delivery(0, 50))      # expect 50
    print(process_delivery(50, 100))    # expect 150
    print(process_delivery(200, 0))     # expect 200 (edge case: zero delivery)


from Capstone_feature import*

# ADD ITEM PRODUCTS FUNCTION
def add_all_menu():
    while True:
        try:
            display_full()
            found_in_products = False
            while True:
                user_add_location = get_alpha_input("Enter the location (or 'back' to ADMIN MENU): ")
                if user_add_location is None:
                    return
                if user_add_location:
                    break
            while True:
                user_add_capital = get_alpha_input("Enter the Capital (or 'back' to ADMIN MENU): ")
                if user_add_location is None:
                    return
                if user_add_capital:
                    break
            while True:
                user_add_type = "type "+str(get_int_input("Enter the type (eq: 120) (Note: Type means an area size(m2)) (or 'back' to ADMIN MENU): "))
                if user_add_type.lower() == 'back':
                    return
                if user_add_type:
                    break
            while True:
                user_add_stock = get_int_input("Add stock of properties (or 'back' to MAIN MENU): ")
                if user_add_stock is None:
                    return
                if user_add_stock:
                    break
            for prop in products:
                if (user_add_location == prop["location"] and 
                    user_add_capital == prop["capital"] and 
                    user_add_type == prop["type"]):
                    prop["stock"] += user_add_stock
                    found_in_products = True
                    break
            if not found_in_products:
                while True:
                    user_add_detail = get_str_input("Enter the detail (eq: 3 x 7 m2  ) (its a wide x length in m2) (or 'back' to MAIN MENU): ")
                    if user_add_detail is None:
                        return
                    if user_add_detail:
                        break
                while True:
                    user_add_sell_price = get_int_input("Enter the selling price (or 'back' to MAIN MENU): ")
                    if user_add_sell_price is None:
                        return
                    if user_add_sell_price:
                        break
                while True:
                    user_add_rent_price = get_int_input("Enter the renting price (or 'back' to MAIN MENU): ")
                    if user_add_rent_price is None:
                        return
                    if user_add_rent_price:
                        break
                new_prop = {
                    "location": user_add_location,
                    "capital": user_add_capital,
                    "type": user_add_type,
                    "detail": user_add_detail,
                    "stock": user_add_stock,
                    "sell_price": user_add_sell_price,
                    "rent_price": user_add_rent_price
                }
                products.append(new_prop)
                while True:
                    repeat = input("Do you want to add another property? (yes/no): ")
                    if repeat == 'yes':
                        save_data(products, "products.json")
                        display_full()
                        break
                    elif repeat == "no":
                        save_data(products, "products.json")
                        display_full()
                        return
                    else:
                        warning(["Invalid input. Please enter the 'yes' to add another property or 'no' to back to ADMIN MENU"])
        except ValueError:
            warning(["Invalid input. Please try again!"])

# REMOVE ITEM PRODUCT FUNCTION
def remove_menu():
    while True:
        try:
            display_full()
            while True:
                user_input_location = get_alpha_input("Enter the location (or 'back' to ADMIN MENU): ")
                if user_input_location is None:
                    return
                found_location = False
                for location_prop in products:
                    if user_input_location.lower() == location_prop["location"].lower():
                        found_location = True
                        while True:
                            user_input_capital = get_alpha_input("Enter the capital (or 'back' to ADMIN MENU): ")
                            if user_input_capital is None:
                                return
                            found_capital = False
                            for capital_prop in products:
                                if user_input_capital.lower() == capital_prop["capital"].lower():
                                    found_capital = True
                                    while True:
                                        user_input_type = "type "+str(get_int_input("Enter the type (eq: 120) (or 'back' to ADMIN MENU): "))
                                        if user_input_type.lower() == "back":
                                            return
                                        found_type = False
                                        for prop in products:
                                            if (user_input_type.lower() == prop["type"].lower() and
                                                user_input_location.lower() == prop["location"].lower() and
                                                user_input_capital.lower() == prop["capital"].lower()):
                                                found_type = True
                                                print(f"Property to Remove:")
                                                print(f"Location: {prop['location']}")
                                                print(f"Capital: {prop['capital']}")
                                                print(f"Type: {prop['type']}")
                                                print(f"Detail: {prop['detail']}")
                                                print(f"Stock: {prop['stock']}")
                                                print(f"Sell Price: {prop['sell_price']}")
                                                print(f"Rent Price: {prop['rent_price']}")
                                                print()
                                                confirmation = get_alpha_input("Are you sure you want to remove this property? (yes/no): ")
                                                while True:
                                                    if confirmation == 'yes':
                                                        products.remove(prop)
                                                        save_data(products, "products.json")
                                                        display_full()
                                                        warning(["Property removed successfully!"])  
                                                        return      
                                                    elif confirmation == "no":
                                                        warning(["Removal canceled."])
                                                        return        
                                                    else:
                                                        warning(["Invalid input. Please enter the 'yes' to delete property or 'no' to cancel"])
                                        if not found_type:
                                            warning(["Invalid Product Type. Please try again."])
                            if not found_capital:
                                warning(["Invalid Capital. Please try again."])
                if not found_location:
                    warning(["Invalid Location. Please try again."])
        except ValueError:
            warning("Invalid input. Please try again!")

# UPDATE ITEM PRODUCTS FUNCTION
def update_menu():
    while True:
        try:
            display_full()
            while True:
                user_input_buy_location = get_alpha_input("Enter the location (or 'back' to MAIN MENU): ")
                if user_input_buy_location is None:
                    return
                found_location = False
                for prop in products:
                    if user_input_buy_location.lower() == prop["location"].lower():
                        found_location = True
                        while True:
                            user_input_buy_capital = get_alpha_input("Enter the capital (or 'back' to MAIN MENU): ")
                            if user_input_buy_capital is None:
                                return
                            found_capital = False
                            for prop in products:
                                if user_input_buy_capital.lower() == prop["capital"].lower():
                                    found_capital = True
                                    while True:
                                        user_input_buy_type = "type "+str(get_int_input("Enter the type (eq: 120) (or 'back' to ADMIN MENU): "))
                                        if user_input_buy_type.lower() == "back":
                                            return
                                        found_type = False
                                        for prop in products:
                                            if (user_input_buy_type.lower() == prop["type"].lower() and
                                                user_input_buy_location.lower() == prop["location"].lower() and
                                                user_input_buy_capital.lower() == prop["capital"].lower()):
                                                found_type = True
                                                print(f"Current Property Details:")
                                                print(f"Location: {prop['location']}")
                                                print(f"Capital: {prop['capital']}")
                                                print(f"Type: {prop['type']}")
                                                print(f"Detail: {prop['detail']}")
                                                print(f"Stock: {prop['stock']}")
                                                print(f"Sell Price: {prop['sell_price']}")
                                                print(f"Rent Price: {prop['rent_price']}")
                                                print()
                                                while True:
                                                    property_to_update = get_str_input("Enter the keys to update (or 'done' to finish): ")
                                                    if property_to_update == 'done':
                                                        return
                                                    elif property_to_update in prop:
                                                        new_value = input(f"Enter the new value for {property_to_update}: ")
                                                        prop[property_to_update] = new_value
                                                        warning([f"{property_to_update} updated to {new_value}."])
                                                        save_data(products, "products.json")
                                                        display_full()
                                                    else:
                                                        warning([f"Invalid property '{property_to_update}'. Please enter valid property names."])
                                        if not found_type:
                                            warning(["Invalid Product Type. Please try again."])
                            if not found_capital:
                                warning(["Invalid Capital. Please try again."])
                if not found_location:
                    warning(["Invalid Location. Please try again."])
        except ValueError:
            warning(["Invalid input. Please try again!"])

# ADMIN MENU
def display_admin_menu():
    display_admin_menu = [[1, "Display product"], [2, "Add new product or stock"], [3, "Remove product"], [4, "Update product's item"],[5, "Exit"]]
    headers = ["Index", '''Admin Menu
(Choose this menu using index)''']
    print(tabulate(display_admin_menu, headers=headers, tablefmt="fancy_grid", colalign=("center", "center")))

def admin_menu():
    while True:
        try :
            display_admin_menu()
            admin_input_menu = get_int_input("Choose admin menu using index: ")
            if admin_input_menu == 1:
                display_menu_display()
            elif admin_input_menu == 2:
                add_all_menu()
            elif admin_input_menu == 3:
                remove_menu()
            elif admin_input_menu == 4:
                update_menu()
            elif admin_input_menu == 5:
                break
            else:
                warning(["Invalid input. Please choose admin menu only by index number"])
        except ValueError:
            warning(["Invalid input. Please try again!"])

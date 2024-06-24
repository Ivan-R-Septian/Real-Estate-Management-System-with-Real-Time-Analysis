from Capstone_feature import*
def buy_name(prompt):
    while True:
        user_input_buy_name = input(prompt).strip().lower()
        if user_input_buy_name == 'back':
            return None
        else:
            buy_menu(user_input_buy_name)
            return
        
def rent_name(prompt):
    while True:
        user_input_rent_name = input(prompt).strip().lower()
        if user_input_rent_name == 'back':
            return None
        else:
            rent_menu(user_input_rent_name)
            return
            
        
def buy_menu(user_input_buy_name):
    headers = ["Location", "Capital", "Type", "Details", "Available", "Sell Price", "Rent Price"]
    colalign = ("center", "center", "center", "center", "right", "center", "center")
    while True:
        try:
            display_full()
            user_input_buy_location = get_str_input("Enter the location (or 'back' to MAIN MENU): ")
            if user_input_buy_location is None:
                return
            words_filter_location = [item for item in table_data if user_input_buy_location  == str(item[0]).lower() ]
            if words_filter_location:
                print(tabulate(words_filter_location, headers=headers, tablefmt="fancy_grid", colalign=colalign))
            found_location = False


            for location in products:
                if user_input_buy_location.lower() == location["location"].lower():
                    found_location = True

                    while True:
                        user_input_buy_capital = get_str_input("Enter the capital (or 'back' to MAIN MENU): ")
                        if user_input_buy_capital is None:
                            return
                        words_filter_capital= [item for item in words_filter_location if user_input_buy_capital == str(item[1]).lower()]
                        if words_filter_capital:
                            print(tabulate(words_filter_capital, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                        found_capital = False

                        for capital in products:
                            if (user_input_buy_capital.lower() == capital["capital"].lower() and
                                user_input_buy_location.lower() == capital["location"].lower()):
                                found_capital = True

                                while True:
                                    user_input_buy_type = get_str_input("Enter the type products (or 'back' to MAIN MENU): ")
                                    if user_input_buy_type is None:
                                        return
                                    words_filter_type= [item for item in words_filter_capital if user_input_buy_type == str(item[2]).lower()]
                                    if words_filter_type:
                                        print(tabulate(words_filter_type, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                                    found_type = False

                                    for prop in products:
                                        if (user_input_buy_type.lower() == prop["type"].lower() and
                                            user_input_buy_location.lower() == prop["location"].lower() and
                                            user_input_buy_capital.lower() == prop["capital"].lower()):
                                            found_type = True

                                            while True:
                                                user_input_buy_stock = get_int_input("Enter the number of property (or 'back' to MAIN MENU): ")
                                                if user_input_buy_stock is None:
                                                    return

                                                if prop["stock"] < user_input_buy_stock:
                                                    warning([f"We don't have enough stock for {prop['type']} {prop['capital']} in {prop['location']}"])
                                                else:
                                                    found_in_basket = False
                                                    for item in buy_item:
                                                        if (item[0] == prop["location"].capitalize() and
                                                            item[1] == prop["capital"].capitalize() and
                                                            item[2] == prop["type"].capitalize()):
                                                            item[4] += user_input_buy_stock
                                                            found_in_basket = True
                                                            break

                                                    if not found_in_basket:
                                                        buy_item.append([
                                                            prop["location"].capitalize(),
                                                            prop["capital"].capitalize(),
                                                            prop["type"].capitalize(),
                                                            prop["detail"],
                                                            user_input_buy_stock,
                                                            prop["sell_price"]
                                                        ])

                                                    warning([f"{user_input_buy_stock} {prop['type']} bought successfully!"])
                                                    basket_buy()
                                                    break

                                            while True:
                                                confirmation_input = get_str_input("Would you like to buy another property? (yes/no): ")
                                                if confirmation_input == "no":
                                                    generate_bill_buy(user_input_buy_name)
                                                    while True:
                                                        try:
                                                            user_money = get_int_input("Enter the amount of money: ")
                                                            if user_money == sum(item[4] * item[5] for item in buy_item):
                                                                warning(["Thank you!"])
                                                                buy_item_to_dict(user_input_buy_name)
                                                                calculate_products()
                                                                buy_item.clear()
                                                                user_calculation_list()
                                                                return
                                                            elif user_money < sum(item[4] * item[5] for item in buy_item):
                                                                warning([f"You need to pay {sum(item[4] * item[5] for item in buy_item)} to complete."])
                                                            else:
                                                                warning([f"Your change is {user_money - sum(item[4] * item[5] for item in buy_item)}."])
                                                                buy_item_to_dict(user_input_buy_name)
                                                                calculate_products()
                                                                buy_item.clear()
                                                                user_calculation_list.clear()
                                                                return
                                                        except ValueError:
                                                            warning(["Please enter a valid amount for money."])
                                                elif confirmation_input == "yes":
                                                    return buy_menu(user_input_buy_name)
                                                else:
                                                    warning(["Invalid input. Please try again"])
                                    if not found_type:
                                        warning(["Invalid Product Type. Please try again."])
                        if not found_capital:
                            warning(["Invalid Capital. Please try again."])
            if not found_location:
                warning(["Invalid Location. Please try again."])
        except ValueError:
            warning(["Please enter a valid input. Please try again."])

def rent_menu(user_input_rent_name):
    headers = ["Location", "Capital", "Type", "Details", "Available", "Sell Price", "Rent Price"]
    colalign = ("center", "center", "center", "center", "right", "center", "center")
    while True:
        try:
            display_full()
            user_input_rent_location = get_str_input("Enter the location (or 'back' to MAIN MENU): ")
            if user_input_rent_location is None:
                return
            words_filter_location = [item for item in table_data if user_input_rent_location == str(item[0]).lower()]
            if words_filter_location:
                print(tabulate(words_filter_location, headers=headers, tablefmt="fancy_grid", colalign=colalign))
            found_location = False


            for location in products:
                if user_input_rent_location.lower() == location["location"].lower():
                    found_location = True

                    while True:
                        user_input_rent_capital = get_str_input("Enter the capital (or 'back' to MAIN MENU): ")
                        if user_input_rent_capital is None:
                            return
                        words_filter_capital= [item for item in words_filter_location if user_input_rent_capital == str(item[0]).lower()]
                        if words_filter_capital:
                            print(tabulate(words_filter_capital, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                        found_capital = False

                        for capital in products:
                            if (user_input_rent_capital.lower() == capital["capital"].lower() and
                                user_input_rent_location.lower() == capital["location"].lower()):
                                found_capital = True

                                while True:
                                    user_input_rent_type = get_str_input("Enter the type products (or 'back' to MAIN MENU): ")
                                    if user_input_rent_type is None:
                                        return
                                    words_filter_type= [item for item in words_filter_capital if user_input_rent_type == str(item[2]).lower()]
                                    if words_filter_type:
                                        print(tabulate(words_filter_type, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                                    found_type = False
                                
                                    for prop in products:
                                        if (user_input_rent_type.lower() == prop["type"].lower() and
                                            user_input_rent_location.lower() == prop["location"].lower() and
                                            user_input_rent_capital.lower() == prop["capital"].lower()):
                                            found_type = True
                                            
                                            while True:
                                                user_input_rent_stock = get_int_input("Enter the number of property (or 'back' to MAIN MENU): ")
                                                if user_input_rent_stock is None:
                                                    break
                                                elif prop["stock"] < user_input_rent_stock:
                                                    warning([f"We don't have enough stock for {prop['type']} {prop['capital']} in {prop['location']}"])
                                                else:
                                                    user_input_rent_duration = get_int_input("Enter the rental duration (or 'back' to MAIN MENU): ")
                                                    if user_input_rent_duration is None:
                                                        break
                                                    else:
                                                        found_in_basket = False
                                                        # Check if the item is already in the basket
                                                        for item in rent_item:
                                                            if (item[0] == prop["location"].capitalize() and
                                                                item[1] == prop["capital"].capitalize() and
                                                                item[2] == prop["type"].capitalize() and
                                                                item[6] == user_input_rent_duration):
                                                                item[4] += user_input_rent_stock
                                                                found_in_basket = True
                                                                break
                                                        if not found_in_basket:
                                                            # Add the new item to the basket
                                                            rent_item.append([
                                                                prop["location"].capitalize(),
                                                                prop["capital"].capitalize(),
                                                                prop["type"].capitalize(),
                                                                prop["detail"],
                                                                user_input_rent_stock,
                                                                prop["rent_price"],
                                                                user_input_rent_duration
                                                            ])
                                                        warning([f"{user_input_rent_stock} {prop['type']} bought successfully!"])
                                                        basket_rent()
                                                        break
                                            while True:
                                                confirmation_input = input("Would you like to rent another property? (yes/no): ")
                                                if confirmation_input.lower() == "no":
                                                    generate_bill_rent(user_input_rent_name)
                                                    while True:
                                                        try:
                                                            user_money = int(input("Enter the amount of money: "))
                                                            if user_money == sum(item[4] * item[5] * item[6] for item in rent_item):
                                                                rent_item_to_dict(user_input_rent_name)
                                                                calculate_products()
                                                                warning(["Thank you!"])
                                                                rent_item.clear()
                                                                user_calculation_list.clear()
                                                                return
                                                            elif user_money < sum(item[4] * item[5] * item[6] for item in rent_item):
                                                                warning([f"You need to pay {sum(item[4] * item[5] * item[6] for item in rent_item)} to complete."])
                                                            else:
                                                                rent_item_to_dict(user_input_rent_name)
                                                                calculate_products()
                                                                warning([f"Your change is {user_money - sum(item[4] * item[5] * item[6] for item in rent_item)}."])
                                                                rent_item.clear()
                                                                user_calculation_list.clear()
                                                                return
                                                        except ValueError:
                                                            warning(["Please enter a valid amount for money."])
                                                elif confirmation_input.lower() == "yes":
                                                    return rent_menu(user_input_rent_name)
                                                else:
                                                    warning(["Invalid input. Please try again"])
                                    if not found_type:
                                        warning(["Invalid Product Type. Please try again."])
                        if not found_capital:
                            warning(["Invalid Capital. Please try again."])
            if not found_location:
                warning(["Invalid Location. Please try again."])
        except ValueError:
            warning(["Please enter a valid input. Please try again."])

def display_customer_menu():
    display_customer_menu = [[1, "Display product"], [2, "Buy property"], [3, "Rent property"], [4, "Exit"]]
    headers = ["Index", '''Customer Menu
(Choose this menu using index)''']
    print(tabulate(display_customer_menu, headers=headers, tablefmt="fancy_grid", colalign=("center", "center")))

def customer_menu():
    while True:
        try :
            display_customer_menu()
            admin_input_menu = get_int_input("Choose customer menu using index: ")
            if admin_input_menu == 1:
                display_menu_display()
            elif admin_input_menu == 2:
                buy_name("Enter your username (or 'back' to MAIN MENU): ")
            elif admin_input_menu == 3:
                rent_name("Enter your username (or 'back' to MAIN MENU): ")
            elif admin_input_menu == 4:
                break
            else:
                warning(["Invalid input. Please choose admin menu only by index number"])
        except ValueError:
            warning(["Invalid input. Please try again!"])

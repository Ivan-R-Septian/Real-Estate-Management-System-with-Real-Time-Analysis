from tabulate import tabulate
from Capstone_dataset import*

# error function
def warning(comment):
    print(tabulate([comment], tablefmt="fancy_grid"))

def get_alpha_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return None
        if user_input.replace(' ', '').isalpha():
            return user_input
        else:
            print("Please enter alphabetic characters only.")


def get_str_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return None
        else:
            return user_input
        
def get_int_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return None
        elif not isinstance(user_input, int) and not user_input.isdigit():
            warning(["Input must be a positive integer"])
        else:
            try:
                return int(user_input)
            except ValueError:
                try:
                    float_value = float(user_input)
                    if float_value.is_integer():
                        return int(float_value)
                    else:
                        return float_value
                except ValueError:
                    return user_input

# function to split string
def custom_type(value):
        try:
            return int(value.split()[1])
        except ValueError:
            return value
        
def rental_duration():
    current_datetime = datetime.now()
    for user_item in dict_list:
        date_str = user_item["end_date"]
        date_obj = datetime.fromisoformat(date_str)
        if date_obj < current_datetime:
            for product in products:
                if (user_item["location"] == product["location"] and
                    user_item["capital"] == product["capital"] and
                    user_item["type"] == product["type"]):
                    product["stock"] += user_item["stock"]
            user_item["stock"] = 0
    save_data(products, "products.json")
    save_data(dict_list, "user.json")

rental_duration()

def calculate_products():
    found = False
    for user_item in user_calculation_list:
        # Iterate through products
        for product in products:
            # Check if location, capital, and type match
            if (user_item["location"] == product["location"] and
                user_item["capital"] == product["capital"] and
                user_item["type"] == product["type"]):
                # Subtract user's stock from product's stock
                product["stock"] -= user_item["stock"]
                found = True
                # Saving data to somewhere (not implemented in this code)
                save_data(products, "products.json")
    if not found:
        warning(["wrong value"])

def basket_buy():
    if buy_item:
            headers = ["City","Capital", "Type", "Details", "Available", "Sell Price"]
            print(tabulate(buy_item,headers=headers, tablefmt="github"))
    else:
        warning(["Your basket is empty."])

def basket_rent():
    if rent_item:
            headers = ["City","Capital", "Type", "Details", "Available", "Rent Price", "Rent Duration"]
            print(tabulate(rent_item,headers=headers, tablefmt="grid"))
    else:
        warning(["Your basket is empty."])

def rent_item_to_dict(user_input_rent_name):
    date_now = datetime.now()
    for item in rent_item:
        rental_duration = timedelta(minutes=item[6])
        rent_end = date_now+rental_duration
        rent_end_str = rent_end.strftime("%Y-%m-%d %H:%M:%S")
        start_date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        dict_item = {
            "name": user_input_rent_name,
            "location": item[0].lower(),
            "capital": item[1].lower(),
            "type": item[2].lower(),
            "detail": item[3].lower(),
            "stock": item[4],
            "total_sell_price": 0,
            "total_rent_price": item[5]*item[4]*item[6],
            "start_date":start_date_str,
            "end_date" : rent_end_str
        }
        dict_list.append(dict_item)
        user_calculation_list.append(dict_item)
    save_data(dict_list, "user.json")
    save_data(user_calculation_list, "user_calculation.json")

def buy_item_to_dict(user_input_buy_name):
    date_now = datetime.now()
    start_date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
    future_date = date_now + timedelta(days=365 * 1000)
    future_date_str = future_date.strftime("%Y-%m-%d %H:%M:%S")
    for item in buy_item:
        dict_item = {
            "name": user_input_buy_name,
            "location": item[0].lower(),
            "capital": item[1].lower(),
            "type": item[2].lower(),
            "detail": item[3].lower(),
            "stock": item[4],
            "total_sell_price": item[5]*item[4],
            "total_rent_price": 0,
            "start_date":start_date_str,
            "end_date" : future_date_str
        }
        dict_list.append(dict_item)
        user_calculation_list.append(dict_item)
    save_data(dict_list, "user.json")
    save_data(user_calculation_list, "user_calculation.json")

def generate_bill_buy(user_input_buy_name):
    print("\n")
    print("******************************************************************************")
    print(f"Bill: {int(random.random()*100000)}\t\t\t\tDate: {datetime.now()}")
    print(f"Customer Name: {user_input_buy_name.capitalize()}")
    total_bill = 0
    headers = ["City","Capital", "Type", "Details", "Available", "Sell Price"]
    print(tabulate(buy_item,headers=headers, tablefmt="fancy_grid"))
    for item in buy_item:
        total_bill += item[4] * item[5]
    print("******************************************************************************")
    print(f"\t\t\t\t\t\tTotal Bill Amount: {total_bill}")
    print("\n")

def generate_bill_rent(user_input_rent_name):
    print("\n")
    print("*********************************************************************************************")
    print(f"Bill: {int(random.random()*100000)}\t\t\t\tDate: {datetime.now()}")
    print(f"Customer Name: {user_input_rent_name.capitalize()}")
    total_bill = 0
    headers = ["City","Capital", "Type", "Details", "Available", "Rent Price", "Rent Duration"]
    print(tabulate(rent_item,headers=headers, tablefmt="fancy_grid"))
    for item in rent_item:
        total_bill += item[4] * item[5] * item[6]
    print("*********************************************************************************************")
    print(f"\t\t\t\t\t\t\Total Bill Amount: {total_bill}")
    print("\n")


# DISPLAY DATASET OF PRODUCT 
def display():
    headers = ["Location", "Capital", "Type", "Details", "Available", "Sell Price", "Rent Price"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", colalign=("center", "center", "center", "center", "right", "center", "center")))
    return table_data

def display_full():
    table_data.clear()
    for prop in products:
        if prop["stock"] == 0:
            available = "Sold Out"
        else:
            available = prop["stock"]
        table_data.append([
            prop["location"].capitalize(),
            prop["capital"].capitalize(),
            prop["type"].capitalize(),
            prop["detail"],
            available,
            f'{prop["sell_price"]:,.0f}',
            f'{prop["rent_price"]:,.0f}'
        ])
    table_data.sort(key=lambda x:x[0])
    display()

def display_menu_display():
    display_full()
    while True:    
        try:
            display_menu = [[1,"Sort"],[2,"Search"],[3,"Filter"]]
            headers = ["Index", '''DISPLAY MENU
(Choose this menu using index)''']
            print(tabulate(display_menu, headers=headers, tablefmt="grid", colalign=("center", "center")))
            back_to_main_menu = False  # Flag to control loop behavior
            while not back_to_main_menu:  # Continue loop until flag is True
                user_input_display = get_int_input("Choose the display menu using index (or 'back' to MAIN MENU): ")
                if user_input_display is None:
                    back_to_main_menu = True  # Set flag to True to exit loop
                elif user_input_display == 1:
                    display_sort_menu()
                    sort_all_menu()
                    break
                elif user_input_display == 2:
                    search_all_menu()
                    break
                elif user_input_display == 3:
                    filter_all_menu()
                    break
                else:
                    warning(["Invalid input. Please choose display menu only by menu index or 'back'"])
            if back_to_main_menu:
                break  # Exit the outer loop if 'back' was selected
        except ValueError:
            warning(["Invalid input. Please try again!"])


# SORT FUNCTION
def display_sort_menu():
    display_sort_menu = [
        [1, "Type or Area Size (asc)"],
        [2, "Type or Area Size (desc)"],
        [3, "Available (asc)"],
        [4, "Available (desc)"],
        [5, "Sell Price (asc)"],
        [6, "Sell Price (desc)"],
        [7, "Rent Price (asc)"],
        [8, "Rent Price (desc)"]
    ]
    headers = ["Index", '''SORT MENU
(Choose this menu using index)''']
    print(tabulate(display_sort_menu, headers=headers, tablefmt="grid", colalign=("center", "center")))

def sort_all_menu():
    while True:
        try :
            user_input_sort_option = get_int_input("Choose the sort menu using index (or 'back' to DISPLAY MENU): ")
            if user_input_sort_option is None:
                table_data.sort(key=lambda x:x[0]) #back it sort based on location asc
                break
            elif user_input_sort_option == 1:
                table_data.sort(key=lambda x: custom_type(x[2]))
                display()
            elif user_input_sort_option == 2:
                table_data.sort(key=lambda x: custom_type(x[2]), reverse=True)
                display()
            elif user_input_sort_option == 3:
                table_data.sort(key=lambda x: int(x[4]))
                display()
            elif user_input_sort_option == 4:
                table_data.sort(key=lambda x: -int(x[4]))
                display()
            elif user_input_sort_option == 5:
                table_data.sort(key=lambda x: int(x[5].replace(',', '')))
                display()
            elif user_input_sort_option == 6:
                table_data.sort(key=lambda x: -int(x[5].replace(',', '')))
                display()
            elif user_input_sort_option == 7:
                table_data.sort(key=lambda x: int(x[6].replace(',', '')))
                display()
            elif user_input_sort_option == 8:
                table_data.sort(key=lambda x: -int(x[6].replace(',', '')))
                display()
            else:
                warning(["Invalid input. Please choose display menu only by menu index or 'back'"])
                continue
            while True:
                repeat = input("Do you want to apply another sort? (yes/no): ")
                if repeat == 'yes':
                    display_sort_menu()
                    break
                elif repeat == "no":
                    return
                else:
                    warning(["Invalid input. Please enter the 'yes' to apply another sort or 'no' to back to SHORT MENU"])
        except ValueError:
            warning(["Enter a valid input. Please try again!"])

# SEARCH FUNCTION
def search_all_menu():
    headers = ["Location", "Capital", "Type", "Details", "Available", "Sell Price", "Rent Price"]
    colalign = ("center", "center", "center", "center", "right", "center", "center")
    display_full()
    while True:
        try:
            user_input_search = get_str_input("Find targeted word (or 'back' to DISPLAY MENU): ")
            if user_input_search is None:
                break
            else:
                words_filter = [item for item in table_data if any(user_input_search in str(attr).lower() for attr in item)]
                if words_filter:
                    print(tabulate(words_filter, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                    while True:
                        repeat = get_str_input("Do you want to apply another filter? (yes/no): ")
                        if repeat == 'yes':
                            display_sort_menu()
                            break
                        elif repeat == "no":
                            return
                        else:
                            print("Invalid input. Please enter the 'yes' to find something else or 'no' to back to FILTER MENU")
                else:
                    warning(["No results found. Please try again"])
        except ValueError:
            warning(["Invalid input. Please try again!"])

# FILTER FUNCTION
def display_filter_menu():
    display_filter_menu = [[1,"Selling price range"],[2,"Renting price range"],[3,"Area size"]]
    headers = ["Index", '''FILTER MENU
(Choose this menu using index)''']
    print(tabulate(display_filter_menu, headers=headers, tablefmt="fancy_grid", colalign=("center", "center")))

def filter_all_menu():
    headers = ["City", "Capital", "Type", "Details", "Available", "Sell Price", "Rent Price"]
    colalign = ("center", "center", "center", "center", "right", "center", "center")  
    while True:
        try:
            display_full()
            display_filter_menu()
            user_input_filter = get_int_input("Choose the filter menu using index (or 'back' to DISPLAY MENU): ")
            if user_input_filter is None:
                break
            elif user_input_filter == 1:
                apply_price_filter("selling", headers, colalign)
            elif user_input_filter == 2:
                apply_price_filter("renting", headers, colalign)
            elif user_input_filter == 3:
                apply_area_filter(headers, colalign)
            else:
                warning(["Invalid input. Please choose filter menu only by menu index or 'back'"])
        except ValueError:
            warning(["Invalid input. Please try again!"])

def apply_price_filter(price_type, headers, colalign):
    while True:
        try:
            display_full()
            max_value = max(int(item[5 if price_type == 'selling' else 6].replace(',', '')) for item in table_data)
            min_value = min(int(item[5 if price_type == 'selling' else 6].replace(',', '')) for item in table_data)
            while True:
                min_price = get_int_input(f"Enter the lowest {price_type} price: (or 'back' to FILTER MENU): ")
                if min_price is None:
                    return  
                elif min_price < 0:
                    warning([f"Lowest {price_type} price must be a positive integer"])
                    continue 
                elif min_price > max_value:
                    warning([f"lowest {price_type} price is larger than the highest price in the table. Please input no more than {max_value}"])
                    continue
                else:
                    while True:
                        max_price_input = get_int_input(f"Enter the highest {price_type} price (or 'back' to FILTER MENU): ")
                        if max_price_input is None:
                            return  
                        elif max_price_input < 0:
                            warning([f"Highest {price_type} price must be a positive integer"])
                            continue
                        elif min_price > max_price_input:
                            warning([f"Lowest {price_type} price cannot be higher than the highest {price_type} price"])
                            continue
                        elif min_value > max_price_input:
                            warning([f"Higest {price_type} price is lower than the lowest price in the table. Please input more than {min_value}"])
                            continue
                        max_price = max_price_input
                        filtered_data = [item for item in table_data if min_price <= int(item[5 if price_type == 'selling' else 6].replace(',', '')) <= max_price]
                        print(tabulate(filtered_data, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                        break
                while True:
                    repeat = get_str_input("Do you want to apply another filter? (yes/no): ")
                    if repeat == 'yes':
                        break
                    elif repeat == "no":
                        display_filter_menu()
                        return
                    else:
                        warning(["Invalid input. Please enter 'yes' to apply another filter or 'no' to go back to FILTER MENU"])
                break
        except (IndexError):
            warning([f"Item not found!. Please enter the range between {min_value} and {max_value}. Note: Smaller range may cause item not found."])
        except ValueError:
            warning(["Invalid input. Please try again!"])

def apply_area_filter(headers, colalign):
    while True:
        try:
            display_full()
            max_value = max(custom_type(item[2]) for item in table_data)
            min_value = min(custom_type(item[2]) for item in table_data)
            while True:
                min_area = get_int_input("Enter the smallest area: (or 'back' to FILTER MENU): ")
                if min_area is None:
                    return
                elif min_area < 0:
                    warning(["Smallest area must be a positive integer"]) 
                    continue
                elif min_area > max_value:
                    warning([f"Smallest area is larger than the highest price in the table. Please input no more than {max_value}"])
                    continue
                else:
                    while True:
                        max_area_input = get_int_input("Enter the biggest area (or 'back' to FILTER MENU): ")
                        if max_area_input is None:
                            return 
                        elif max_area_input < 0:
                            warning(["The biggest area must be a positive integer"])
                            continue
                        elif min_area > max_area_input:
                            warning([f"Smallest area cannot be higher than the biggest area"])
                            continue
                        elif min_value > max_area_input:
                            warning([f"Biggest area is smaller than the smallest value in the table. Please input no more than {min_value}"])
                            continue
                        max_area = max_area_input
                        filtered_data = [item for item in table_data if min_area <= custom_type(item[2]) <= max_area]
                        print(tabulate(filtered_data, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                        break
                while True:
                    repeat = get_str_input("Do you want to apply another filter? (yes/no): ")
                    if repeat == 'yes':
                        break
                    elif repeat == "no":
                        display_filter_menu()
                        return
                    else:
                        warning(["Invalid input. Please enter 'yes' to apply another filter or 'no' to go back to FILTER MENU"])
                break
        except (IndexError):
            warning([f"Item not found!. Please enter the range between {min_value} and {max_value}. Note: Smaller range may cause item not found."])
        except ValueError:
            warning(["Invalid input. Please try again!"])
            
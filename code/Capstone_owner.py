from Capstone_customer import*
from Capstone_admin import*

def display_full_owner():
    table_user.clear()
    for index, prop in enumerate(dict_list, start=1):
        if prop["stock"] == 0:
            available = "rent expired"
        else:
            available = prop["stock"]
        table_user.append([
            prop["name"].capitalize(),
            prop["location"].capitalize(),
            prop["capital"].capitalize(),
            prop["type"].capitalize(),
            prop["detail"],
            available,
            f'{prop["total_sell_price"]:,.0f}',
            f'{prop["total_rent_price"]:,.0f}',
            prop["start_date"],
            prop["end_date"]
        ])
    table_user.sort(key=lambda x:x[0])    
    display_owner()

def display_owner():
    headers = ["Name","City", "Capital", "Type", "Details", "Available", "Sell Price", "Rent Price", "Start date", "End date"]
    print(tabulate(table_user, headers=headers, tablefmt="fancy_grid", colalign=("center","center", "center", "center", "center", "right", "center", "center", "center", "center")))
    return table_user


def display_menu_display_owner():
    display_full_owner()
    while True:    
        try:
            rental_duration()
            display_menu = [[1,"Sort"],[2,"Search"]]
            headers = ["Index", '''DISPLAY MENU
(Choose this menu using index)''']
            print(tabulate(display_menu, headers=headers, tablefmt="grid", colalign=("center", "center")))
            back_to_main_menu = False  # Flag to control loop behavior
            while not back_to_main_menu:  # Continue loop until flag is True
                user_input_display = get_int_input("Choose the display menu using index (or 'back' to MAIN MENU): ")
                if user_input_display is None:
                    back_to_main_menu = True  # Set flag to True to exit loop
                elif user_input_display == 1:
                    display_sort_menu_owner()
                    sort_all_menu_owner()
                    break
                elif user_input_display == 2:
                    search_all_menu_owner()
                    break
                else:
                    warning(["Invalid input. Please choose display menu only by menu index or 'back'"])
            if back_to_main_menu:
                break  # Exit the outer loop if 'back' was selected
        except ValueError:
            warning(["Invalid input. Please try again!"])

# SORT FUNCTION
def display_sort_menu_owner():
    display_sort_menu = [
        [1, "User name (asc)"],
        [2, "User name (desc)"],
        [3, "City (asc)"],
        [4, "City (desc)"],
        [5, "Capital (asc)"],
        [6, "Capital (desc)"],
        [7, "Type (asc)"],
        [8, "Type (desc)"]
    ]
    headers = ["Index", '''SORT MENU
(Choose this menu using index)''']
    print(tabulate(display_sort_menu, headers=headers, tablefmt="grid", colalign=("center", "center")))

def sort_all_menu_owner():
    while True:
        try :
            user_input_sort_option = get_int_input("Choose the sort menu using index (or 'back' to DISPLAY MENU): ")
            if user_input_sort_option is None:
                table_user.sort(key=lambda x:x[0]) #back it sort based on location asc
                break
            elif user_input_sort_option == 1:
                table_user.sort(key=lambda x: x[0])
                display_owner()
            elif user_input_sort_option == 2:
                table_user.sort(key=lambda x:x[0],reverse=True)
                display_owner()
            elif user_input_sort_option == 3:
                table_user.sort(key=lambda x: x[1])
                display_owner()
            elif user_input_sort_option == 4:
                table_user.sort(key=lambda x:x[1],reverse=True)
                display_owner()
            elif user_input_sort_option == 5:
                table_user.sort(key=lambda x:x[2])
                display_owner()
            elif user_input_sort_option == 6:
                table_user.sort(key=lambda x:x[2],reverse=True)
                display_owner()
            elif user_input_sort_option == 7:
                table_user.sort(key=lambda x: custom_type(x[3]))
                display_owner()
            elif user_input_sort_option == 8:
                table_user.sort(key=lambda x: custom_type(x[3]), reverse=True)
                display_owner()
            else:
                warning(["Invalid input. Please choose display menu only by menu index or 'back'"])
                continue
            while True:
                repeat = get_str_input("Do you want to apply another sort? (yes/no): ")
                if repeat == 'yes':
                    display_sort_menu_owner()
                    break
                elif repeat == "no":
                    return
                else:
                    warning(["Invalid input. Please enter the 'yes' to apply another sort or 'no' to back to SHORT MENU"])
        except ValueError:
            warning(["Enter a valid input. Please try again!"])

# SEARCH FUNCTION
def search_all_menu_owner():
    headers = ["Name", "City", "Capital", "Type", "Details", "Available", "Sell Price", "Rent Price","End date"]
    colalign = ("center", "center", "center", "center", "center","right", "center", "center","center")
    display_full_owner()
    while True:
        try:
            user_input_search = get_str_input("Find targeted word (or 'back' to DISPLAY MENU): ")
            if user_input_search is None:
                break
            else:
                words_filter = [item for item in table_user if any(user_input_search in str(attr).lower() for attr in item)]
                if words_filter:
                    print(tabulate(words_filter, headers=headers, tablefmt="fancy_grid", colalign=colalign))
                    while True:
                        repeat = get_str_input("Do you want to apply another filter? (yes/no): ")
                        if repeat == 'yes':
                            display_full_owner()
                            break
                        elif repeat == "no":
                            return
                        else:
                            warning(["Invalid input. Please enter the 'yes' to find something else or 'no' to back to FILTER MENU"])
                else:
                    warning(["No results found. Please try again"])
        except ValueError:
            warning(["Invalid input. Please try again!"])

def total_profit():
    total_sell_price = 0
    total_rent_price = 0
    # Iterate over each dictionary in the list and sum the values
    for entry in dict_list:
        total_sell_price += entry["total_sell_price"]
        total_rent_price += entry["total_rent_price"]

    warning(["Total Sell Price:", total_sell_price])
    warning(["Total Rent Price:", total_rent_price])

def profit_plot():
    for item in dict_list:
        item["start_date"] = datetime.fromisoformat(item["start_date"])

# Calculate total rent price, sell price, and total price per min
    prices_per_min = {}
    for item in dict_list:
        min = item["start_date"].strftime("%Y-%m-%d %H:%M:00")
        rent_price = item["total_rent_price"]
        sell_price = item["total_sell_price"]
        total_price = rent_price + sell_price
        if min in prices_per_min:
            prices_per_min[min]["total_rent_price"] += rent_price
            prices_per_min[min]["total_sell_price"] += sell_price
            prices_per_min[min]["total_price"] += total_price
        else:
            prices_per_min[min] = {"total_rent_price": rent_price, "total_sell_price": sell_price, "total_price": total_price}

    # Sort data by min
    sorted_prices_per_min = {k: v for k, v in sorted(prices_per_min.items(), key=lambda item: item[0])}

    # Extract x and y values for plotting
    mins = list(sorted_prices_per_min.keys())
    rent_prices = [price["total_rent_price"] for price in sorted_prices_per_min.values()]
    sell_prices = [price["total_sell_price"] for price in sorted_prices_per_min.values()]
    total_prices = [price["total_price"] for price in sorted_prices_per_min.values()]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(mins, rent_prices, marker='o', linestyle='-', label='total_Rent Price', markersize=10, linewidth=2)
    plt.plot(mins, sell_prices, marker='o', linestyle='-', label='total_Sell Price', markersize=10, linewidth=2)
    plt.plot(mins, total_prices, marker='o', linestyle='-', label='Total Price', markersize=5, linewidth=1)
    plt.title('Prices per min')
    plt.xlabel('min')
    plt.ylabel('Price')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    for item in dict_list:
        item["start_date"] = item["start_date"].strftime("%Y-%m-%d %H:%M:%S")
    

def view_profit():
    while True:
        display_full_owner()
        total_profit()
        graph = get_str_input("Do you want to see the profit graph? (yes/no) ")
        if graph == "no":
            rental_duration()
            break
        elif graph == "yes":
            profit_plot()
        else:
            warning(["No results found. Please try again"])

def display_owner_menu():
    display_owner_menu = [[1, "Display product"], [2, "Add new product or stock"], [3, "Remove product or reduce stock"], [4, "Update product's item"], [5, "Buy property"], [6, "Rent property"], [7, "Display customer"], [8, "Display profit"],[9, "Exit"]]
    headers = ["Index", '''Owner Menu
(Choose this menu using index)''']
    print(tabulate(display_owner_menu, headers=headers, tablefmt="fancy_grid", colalign=("center", "center")))

def owner_menu():
    while True:
        try :
            display_owner_menu()
            owner_input_menu = get_int_input("Choose owner menu using index: ")
            if owner_input_menu == 1:
                display_menu_display()
            elif owner_input_menu == 2:
                add_all_menu()
            elif owner_input_menu == 3:
                remove_menu()
            elif owner_input_menu == 4:
                update_menu()
            elif owner_input_menu == 5:
                buy_name("Enter your username (or 'back' to MAIN MENU): ")
            elif owner_input_menu == 6:
                rent_name("Enter your username (or 'back' to MAIN MENU): ")
            elif owner_input_menu == 7:
                display_menu_display_owner()
            elif owner_input_menu == 8:
                view_profit()     
            elif owner_input_menu == 9:
                break
            else:
                warning(["Invalid input. Please choose menu only by index number"])
        except ValueError:
            warning(["Invalid input. Please try again!"])

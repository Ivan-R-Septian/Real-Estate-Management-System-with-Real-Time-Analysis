from Capstone_admin import*
from Capstone_customer import*
from Capstone_owner import*

def display_main_menu():
    display_main_menu = [[1, "Admin menu"], [2, "Customer menu"],[3, "Owner menu"], [4, "Exit"]]
    headers = ["Index", '''Main Menu
(Choose this menu using index)''']
    print(tabulate(display_main_menu, headers=headers, tablefmt="fancy_grid", colalign=("center", "center")))

def main_menu():
    while True:
        try :
            display_main_menu()
            main_input_menu = get_str_input("Choose main menu using index: ")
            if main_input_menu == "1":
                admin_password = get_int_input("Please enter admin passowrd: ")
                if admin_password == 12345:
                    admin_menu()
                else:
                    warning(["Incorrect password"])
            elif main_input_menu == "2":
                customer_menu()
            elif main_input_menu == "3":
                owner_password = get_int_input("Please enter owner passowrd: ")
                if owner_password == 123456789:
                    owner_menu()
                else:
                    warning(["Incorrect password"])
            elif main_input_menu == "4":
                break
            else:
                warning(["Invalid input. Please choose menu only by index number"])
        except ValueError:
            warning(["Invalid input. Please try again!"])
# update rental time
rental_duration()
if __name__ == "__main__":
    main_menu()
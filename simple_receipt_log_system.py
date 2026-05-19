# simple_receipt_log_system.py
# Updates(Pasia):
# - Add necessary variables
# - Add and replace store name placeholder using grocery_name in main_menu()
# - Add items in dairy, snacks, and hygiene aisles
# - Add meat & seafood and frozen desserts aisles
# - Add vat_added_price on item loop in show_aisle()
# - Add .replace() function on choice input in show_aisle() and main_menu()
# - Add similar elif and else statement from main_menu() to show_aisle() in choice input
# - Add .strip() function on confirm input in show_aisle()
# - Add view_cart() function logic
# - Add check_out() function logic
# - Change enumerate function of printing aisles to range in main_menu()
#   (kasi si Kharvi yata 'yun naglagay ng enumerate sa Midterm exam, 'tas sabi ni Sir. 'di raw niya 'yun tinuro kahit nasa ppt lessons naman may nakalagay, kaya pinaulit gawa niya, 'cuz inattempt niya 'yung oneshot prompt)
# - Add goodbye message when exiting in main_menu()

# - Gian's contribution:
# duplicate item checking in cart
# cart update option
# cart delete option
# cash validation
# insufficient cash rejection
# receipt file saving

# Updates(Aron):
# - Updated Gian's CRUD with validity checks and proper integration(nested if else)
# - Added more "Writes" in addition with what Gian did for a more complete receipt
# - Overall it is integration of Gian's code to work on the main code and made sure the code quality is good.

LINE_DEC = "=" * 50
VAT_RATE = 0.12
VAT_TIN = "123-456-789-01234"
MIN = "12345678901234567"
SN = "AB123CDE"
grocery_name = "Aisle Shop Here"
cart_list = []
cash = 0

# 2D List: [Aisle Name, [ [Item ID, Item Name, Price]]]
# Do add more with strictly the same pattern
INVENTORY = [
    ["Dairy", [["1", "Milk", 50], ["2", "Cheese", 60], ["3", "Butter", 35], ["4", "Yogurt", 50], ["5", "Sour Cream", 42]]],
    ["Snacks", [["1", "Chips", 30], ["2", "Pastillas", 55], ["3", "Crackers", 74], ["4", "Candy", 20], ["5", "Dried Mango", 64]]],
    ["Meat & Seafood", [["1", "Pork", 193], ["2", "Beef", 207], ["3", "Chicken", 188], ["4", "Tuna", 135], ["5", "Squid", 159]]],
    ["Frozen Desserts", [["1", "Ice Cream", 57], ["2", "Gelato", 64], ["3", "Sherbet", 65], ["4", "Sorbet", 60], ["5", "Taiyaki", 50]]],
    ["Hygiene", [["1", "Soap", 25], ["2", "Shampoo", 120], ["3", "Toothbrush", 78], ["4", "Toothpaste", 105], ["5", "Deodorant", 80]]]
]

# show_aisle lacks error handling(especially if it's an unknown string of words), do add on it
def show_aisle(aisle_data):
    """Handles the menu for a specific aisle(ex: Dairy)"""
    name = aisle_data[0]
    items = aisle_data[1]

    while True:
        print(f"\n{LINE_DEC}\n--- {name} Aisle ---")
        print(LINE_DEC)

        for item in items:
            vat_added_price = item[2] * (1 + VAT_RATE)
            print(f"({item[0]}) {item[1]} - ₱{vat_added_price:.2f}")

        print("Type 'back' to go to Main Menu or 'cart' to view items.")
        choice = input("Input: ").lower().strip().replace(" ", "")

        if choice == 'back':
            return

        elif choice == 'cart':
            view_cart()

        elif choice.isdigit() and 0 < int(choice) <= len(items):
            # Check if the input matches an item ID
            found = False
            for item in items:
                if choice == item[0]:
                    found = True
                    confirm = input(f"Buy {item[1]}? (Y/N): ").upper().strip()
                    if confirm == 'Y':
                        qty_text = input("Quantity: ").strip()

                        if qty_text.isdigit() and int(qty_text) > 0:
                            qty = int(qty_text)

                            duplicate = False
                            for i in range(len(cart_list)):
                                if cart_list[i][0] == item[1]:
                                    cart_list[i][2] = cart_list[i][2] + qty
                                    duplicate = True
                                    break

                            if duplicate == False:
                                cart_list.append([item[1], item[2], qty])

                            print("Added to cart!")
                        else:
                            print("Invalid quantity.")
                    break

            if found == False:
                print("Invalid choice.")

        else:
            print("Invalid choice.")

"""view_cart() function here"""
def view_cart():
    total_items = len(cart_list)
    print(f"\n{LINE_DEC}\n--- Your Cart ---")

    if total_items == 0:
        print("Your cart is empty.")
        return

    elif total_items > 0:
        for cart_item in range(len(cart_list)):
            print(f"({cart_item + 1}) {cart_list[cart_item][0]} ×{cart_list[cart_item][2]}")

        print("\n1. Update item")
        print("2. Delete item")
        print("3. Pay")
        print("4. Back")

        choice = input("Input: ").lower().strip().replace(" ", "")

        if choice == '1':
            num_text = input("Item number: ").strip()
            if num_text.isdigit():
                num = int(num_text) - 1
                if num >= 0 and num < len(cart_list):
                    new_qty_text = input("New quantity: ").strip()
                    if new_qty_text.isdigit() and int(new_qty_text) > 0:
                        new_qty = int(new_qty_text)
                        cart_list[num][2] = new_qty
                        print("Item updated.")
                    else:
                        print("Invalid quantity.")
                else:
                    print("Invalid item number.")
            else:
                print("Invalid input.")

        elif choice == '2':
            num_text = input("Remove item number: ").strip()
            if num_text.isdigit():
                num = int(num_text) - 1
                if num >= 0 and num < len(cart_list):
                    cart_list.pop(num)
                    print("Item removed.")
                else:
                    print("Invalid item number.")
            else:
                print("Invalid input.")

        elif choice == '3':
            confirm = input("Buy item(s)? (Y/N): ").upper().strip()
            if confirm == 'Y':
                pay_items()

        elif choice == '4':
            return

        else:
            print("Invalid choice.")

"""Receipt here use: "checkout()"""
def pay_items():
    global cash
    cash_text = input("Cash: ").strip()

    # Restore the first version's simple validation
    if cash_text.replace(".", "", 1).isdigit():
        cash = float(cash_text)
        checkout()
    else:
        print("Invalid cash input.")

def checkout():
    global cash

    if len(cart_list) == 0:
        print("Cart is empty.")
        return

    print(LINE_DEC)
    print(f"{grocery_name:^50}")
    print(f"VAT-REG-TIN: {VAT_TIN}")
    print(f"MIN: {MIN}")
    print(f"S/N: {SN}")
    print(LINE_DEC)

    total_final_price = 0
    total_qty = 0

    for cart_item in range(len(cart_list)):
        item_name = cart_list[cart_item][0]
        item_price = cart_list[cart_item][1]
        item_qty = cart_list[cart_item][2]
        vat_amount = item_price * VAT_RATE
        total_price = item_price + vat_amount
        final_price = total_price * item_qty

        total_final_price += final_price
        total_qty += item_qty

        print(f"{item_name}")
        print(f"{item_qty} × {total_price:<39.2f}{final_price:.2f}")

    if cash < total_final_price:
        print(LINE_DEC)
        print("Not enough cash")
        return

    change = cash - total_final_price
    print(LINE_DEC)
    print(f"{total_qty} Item(s){total_final_price:>38.2f}")
    print(f"Cash {cash:>44.2f}")
    print(f"Change {change:>42.2f}")
    print(LINE_DEC)

    file = open("receipt.txt", "a")
    file.write(grocery_name + "\n")
    file.write("VAT-REG-TIN: " + VAT_TIN + "\n")
    file.write("MIN: " + MIN + "\n")
    file.write("S/N: " + SN + "\n")

    for item in cart_list:
        file.write(item[0] + " x " + str(item[2]) + "\n")

    file.write("Total Items: " + str(total_qty) + "\n")
    file.write("Total: " + str(total_final_price) + "\n")
    file.write("Cash: " + str(cash) + "\n")
    file.write("Change: " + str(change) + "\n")
    file.write("\n")
    file.close()

    cart_list.clear()

def main_menu():
    """The entry point of the program"""
    while True:
        print(f"\n{LINE_DEC}\nWelcome to {grocery_name} 🌹")
        print(LINE_DEC)

        for aisle in range(len(INVENTORY)):
            print(f"({aisle + 1}) {INVENTORY[aisle][0]}")

        print("Type 'cart' to view cart or 'exit' to quit.")

        choice = input("Input: ").lower().strip().replace(" ", "")

        if choice == 'exit':
            print(f"Thank you for choosing {grocery_name}, come back again!")
            break

        elif choice == 'cart':
            view_cart()

        elif choice.isdigit() and 0 < int(choice) <= len(INVENTORY):
            show_aisle(INVENTORY[int(choice) - 1])

        else:
            print("Invalid choice.")

main_menu()
# simple_receipt_log_system.py
# Updates:
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
            for item in items:
                if choice == item[0]:
                    confirm = input(f"Buy {item[1]}? (Y/N): ").upper().strip()
                    if confirm == 'Y':
                        qty = int(input("Quantity: "))
                        cart_list.append([item[1], item[2], qty])
                        print("Added to cart!")
        else:
            print("Invalid choice.")

"""view_cart() function here"""
def view_cart():
    total_items = len(cart_list)
    print(f"\n{LINE_DEC}\n--- Your Cart ---")
    if total_items == 0:
        print("Your cart is empty.")
    
    elif total_items > 0:
        for cart_item in range(len(cart_list)):
            print(f"({cart_item + 1}) {cart_list[cart_item][0]} ×{cart_list[cart_item][2]}")
        print("Type 'back' to go to previous menu or 'pay' to buy items.")
        
        choice = input("Input: ").lower().strip().replace(" ", "")
        if choice == 'back':
            return
        elif choice == 'pay':
            confirm = input("Buy item(s)? (Y/N): ").upper().strip()
            if confirm == 'Y':
                global cash
                user_cash = float(input("Cash: "))
                cash = user_cash
                checkout()
        else:
            print("Invalid choice.")

"""Receipt here use: "checkout()"""
def checkout():
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

        print(f"{item_name}\n{item_qty} × {total_price:<39.2f}{final_price:.2f}V")

# Add Error handling if the user input's negative or insufficient currency
    change = cash - total_final_price
    print(LINE_DEC)
    print(f"{total_qty} Items(s){total_final_price:>38.2f}")
    print(f"Cash {cash:>44.2f}")
    print(f"Change {change:>42.2f}")
    print(LINE_DEC)
    cart_list.clear()


def main_menu():
    """The entry point of the program"""
    while True:
        print(f"\n{LINE_DEC}\nWelcome to {grocery_name} 🌹")
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
            """Basically displays the menu"""
            show_aisle(INVENTORY[int(choice)-1])
        else:
            print("Invalid choice.")
VAT_RATE = 0.12
LINE_DEC = "=" * 50

# 2D List: [Aisle Name, [ [Item ID, Item Name, Price]]]
# Do add more with strictly the same pattern
INVENTORY = [
    ["Dairy", [["1", "Milk", 50], ["2", "Cheese", 60], ["3", "Butter", 35]]],
    ["Snacks", [["1", "Chips", 30], ["2", "Candy", 15]]],
    ["Hygiene", [["1", "Soap", 25], ["2", "Shampoo", 120]]]
]

cart_list = []

# show_aisle lacks error handling(especially if it's an unknown string of words), do add on it
def show_aisle(aisle_data):
    """Handles the menu for a specific aisle(ex: Dairy)"""
    name = aisle_data[0]
    items = aisle_data[1]
    
    while True:
        print(f"\n{LINE_DEC}\n--- {name} Aisle ---")
        for item in items:
            print(f"({item[0]}) {item[1]} - ₱{item[2]}")
        print("Type 'back' to go to Main Menu or 'cart' to view items.")
        
        choice = input("Input: ").lower().strip()
        
        if choice == 'back':
            return
        elif choice == 'cart':
            view_cart()
        else:
            # Check if the input matches an item ID
            for item in items:
                if choice == item[0]:
                    confirm = input(f"Buy {item[1]}? (Y/N): ").upper()
                    if confirm == 'Y':
                        qty = int(input("Quantity: "))
                        cart_list.append([item[1], item[2], qty])
                        print("Added to cart!")




"""view_cart() function here"""
def view_cart():
    pass
# If empty, show/say empty
# Loop the cart_list[] to print the things added to the cart
# Add the 'back' 
# call the checkout() func if the user will pay already,
# then use the return function to go back at entrance('main_menu()')



"""Receipt here use: "checkout()"""
def checkout():
    pass
# Display the receipt
# Use the VAT_RATE
# use the clear() func on the cart list to reset to 0

def main_menu():
    """The entry point of the program"""
    while True:
        print(f"\n{LINE_DEC}\nWelcome to *Our Store* 🌹") # Placeholder
        for i, aisle in enumerate(INVENTORY):
            print(f"({i+1}) {aisle[0]}")
        print("Type 'cart' to view cart or 'exit' to quit.")
        
        choice = input("Input: ").lower().strip()
        
        if choice == 'exit':
            # Add a print a goodbye message here
            break
        elif choice == 'cart':
            view_cart()
        elif choice.isdigit() and 0 < int(choice) <= len(INVENTORY):
            """Basically displays the menu"""
            show_aisle(INVENTORY[int(choice)-1])
        else:
            print("Invalid choice.")

main_menu()
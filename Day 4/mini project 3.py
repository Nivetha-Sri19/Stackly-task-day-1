cart = []

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(item)
    print("Product added to cart!\n")

def display_cart():
    if len(cart) == 0:
        print("Cart is empty.\n")
        return

    print("\nCART ITEMS")
    for i, item in enumerate(cart):
        total = item["price"] * item["quantity"]
        print(f"{i+1}. {item['name']} - Price: {item['price']} - Qty: {item['quantity']} - Total: {total}")
    print()

def remove_item():
    display_cart()
    index = int(input("Enter item number to remove: ")) - 1

    if 0 <= index < len(cart):
        cart.pop(index)
        print("Item removed successfully!\n")
    else:
        print("Invalid item number!\n")

def calculate_total():
    total_bill = 0
    for item in cart:
        total_bill += item["price"] * item["quantity"]

    print("Total Bill:", total_bill, "\n")

def menu():
    while True:
        print("Shopping Cart")
        print("1. Add Product")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Total Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")

menu()
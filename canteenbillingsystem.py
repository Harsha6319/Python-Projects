from datetime import datetime
import os

# ---------------- Menu Catalog ----------------
class MenuCatalog:
    def __init__(self):
        self.items = {
            "Tea": 10,
            "Coffee": 15,
            "Samosa": 20,
            "Sandwich": 40,
            "Meals": 80,
            "Cold Drink": 25,
            "Burger": 60,
            "Pizza": 120
        }

    def show_menu(self):
        print("\n------ CANTEEN MENU ------")
        for item, price in self.items.items():
            print(f"{item} - ₹{price}")

    def get_price(self, name):
        return self.items.get(name, 0)


# ---------------- Payment ----------------
class PaymentMethod:
    def pay(self, amount):
        pass


class UpiPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")
        return True


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing Card payment of ₹{amount}")
        return True


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Cash received: ₹{amount}")
        return True


# ---------------- Canteen Order ----------------
class CanteenOrder:
    order_counter = 1

    def __init__(self, customer):
        self.order_id = f"CNT{CanteenOrder.order_counter}"
        CanteenOrder.order_counter += 1
        self.customer = customer
        self.items = []   # now stores simple dictionaries
        self.created_at = datetime.now()
        self.status = "Created"

    def add_item(self, name, qty, price):
        total = qty * price
        self.items.append({
            "name": name,
            "qty": qty,
            "price": price,
            "total": total
        })

    def total(self):
        return sum(item["total"] for item in self.items)

    def process_payment(self, method):
        if self.status == "Paid":
            print("⚠️ Order already paid")
            return

        if method.pay(self.total()):
            self.status = "Paid"
            print("✅ Payment Successful")
        else:
            self.status = "Payment Failed"

    def show_bill(self):
        print("\n===== BILL =====")
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Date:", self.created_at)
        print("----------------------")

        for item in self.items:
            print(f"{item['name']} x {item['qty']} = ₹{item['total']}")

        print("----------------------")
        print("Total: ₹", self.total())
        print("Status:", self.status)

        self.save_bill_to_file()

    def save_bill_to_file(self):
        try:
            file_path = "canteen_bills.txt"

            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n===== BILL =====\n")
                f.write(f"Order ID: {self.order_id}\n")
                f.write(f"Customer: {self.customer}\n")
                f.write(f"Date: {self.created_at}\n")

                for item in self.items:
                    # safe access using .get()
                    name = item.get("name")
                    qty = item.get("qty")
                    total = item.get("total")
                    f.write(f"{name} x {qty} = ₹{total}\n")

                f.write(f"Total: ₹{self.total()}\n")
                f.write(f"Status: {self.status}\n")
                f.write("----------------------\n")

        except Exception as e:
            print("Error saving bill:", e)


# ---------------- Canteen System ----------------
class CanteenSystem:
    def __init__(self):
        self.menu = MenuCatalog()
        self.orders = {}

    def place_order(self):
        name = input("Enter customer name: ")
        order = CanteenOrder(name)

        while True:
            self.menu.show_menu()
            item = input("Enter item (or done): ")

            if item.lower() == "done":
                break

            if item not in self.menu.items.keys():
                print("Item not available")
                continue

            qty = int(input("Enter quantity: "))
            price = self.menu.get_price(item)
            order.add_item(item, qty, price)

        self.orders[order.order_id] = order
        print("✅ Order placed! ID:", order.order_id)

    def select_order(self):
        oid = input("Enter Order ID: ")
        return self.orders.get(oid)


# ---------------- Main ----------------
def main():
    system = CanteenSystem()

    while True:
        print("\n===== CANTEEN SYSTEM =====")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. Process Payment")
        print("4. Show Bill (and Save)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.menu.show_menu()

        elif choice == "2":
            system.place_order()

        elif choice == "3":
            order = system.select_order()
            if order:
                print("1. UPI\n2. Card\n3. Cash")
                opt = input("Choose payment: ")

                if opt == "1":
                    order.process_payment(UpiPayment())
                elif opt == "2":
                    order.process_payment(CardPayment())
                elif opt == "3":
                    order.process_payment(CashPayment())
                else:
                    print('Invalid Payment Option.')
            else:
                print("Order not found")

        elif choice == "4":
            order = system.select_order()
            if order:
                order.show_bill()
                print("💾 Bill saved to canteen_bills.txt")
            else:
                print("Order not found")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


main()
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# ---------- Theme Colors ----------
BG = "#0f172a"
CARD = "#111827"
PRIMARY = "#22c55e"
ACCENT = "#38bdf8"
TEXT = "#e5e7eb"
BTN = "#1f2937"


# ---------------- Menu ----------------
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

    def get_price(self, name):
        return self.items.get(name, 0)


# ---------------- Order ----------------
class CanteenOrder:
    order_counter = 1

    def __init__(self, customer):
        self.order_id = f"CNT{CanteenOrder.order_counter}"
        CanteenOrder.order_counter += 1
        self.customer = customer
        self.items = []
        self.created_at = datetime.now()
        self.status = "Created"

    def add_item(self, name, qty, price):
        total = qty * price
        self.items.append({"name": name, "qty": qty, "total": total})

    def total(self):
        return sum(item["total"] for item in self.items)

    def process_payment(self):
        if self.status == "Paid":
            return "Already Paid"
        self.status = "Paid"
        return "Payment Successful"

    def save_bill(self):
        with open("canteen_bills.txt", "a", encoding="utf-8") as f:
            f.write(f"\nOrder ID: {self.order_id}\n")
            for item in self.items:
                f.write(f"{item['name']} x {item['qty']} = ₹{item['total']}\n")
            f.write(f"Total: ₹{self.total()}\n")


# ---------------- GUI ----------------
class ModernCanteenGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Canteen Dashboard")
        self.root.geometry("600x550")
        self.root.configure(bg=BG)

        self.menu = MenuCatalog()
        self.order = None

        # Title
        tk.Label(root, text="🍽 Canteen Management Dashboard",
                 bg=BG, fg=ACCENT, font=("Segoe UI", 16, "bold")).pack(pady=10)

        # Card Frame
        card = tk.Frame(root, bg=CARD, padx=20, pady=20)
        card.pack(pady=10, fill="x", padx=20)

        # Customer
        tk.Label(card, text="Customer Name", bg=CARD, fg=TEXT).pack(anchor="w")
        self.customer_entry = tk.Entry(card, bg=BTN, fg=TEXT, insertbackground="white")
        self.customer_entry.pack(fill="x", pady=5)

        # Item Dropdown
        tk.Label(card, text="Select Item", bg=CARD, fg=TEXT).pack(anchor="w")
        self.item_var = tk.StringVar(value=list(self.menu.items.keys())[0])
        tk.OptionMenu(card, self.item_var, *self.menu.items.keys()).pack(fill="x", pady=5)

        # Quantity
        tk.Label(card, text="Quantity", bg=CARD, fg=TEXT).pack(anchor="w")
        self.qty_entry = tk.Entry(card, bg=BTN, fg=TEXT, insertbackground="white")
        self.qty_entry.pack(fill="x", pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg=BG)
        btn_frame.pack(pady=10)

        self.make_button(btn_frame, "Create Order", self.create_order, PRIMARY).grid(row=0, column=0, padx=5)
        self.make_button(btn_frame, "Add Item", self.add_item, ACCENT).grid(row=0, column=1, padx=5)
        self.make_button(btn_frame, "Pay", self.pay_order, "#f59e0b").grid(row=0, column=2, padx=5)
        self.make_button(btn_frame, "Show Bill", self.show_bill, "#ef4444").grid(row=0, column=3, padx=5)

        # Output Box
        self.output = tk.Text(root, height=12, bg=CARD, fg=TEXT, insertbackground="white")
        self.output.pack(fill="both", expand=True, padx=20, pady=10)

    def make_button(self, parent, text, command, color):
        return tk.Button(parent, text=text, command=command,
                         bg=color, fg="white", width=12, bd=0,
                         font=("Segoe UI", 10, "bold"), padx=5, pady=5)

    def create_order(self):
        name = self.customer_entry.get()
        if not name:
            messagebox.showwarning("Error", "Enter customer name")
            return
        self.order = CanteenOrder(name)
        self.output.insert("end", f"\nOrder Created → {self.order.order_id}\n")

    def add_item(self):
        if not self.order:
            messagebox.showwarning("Error", "Create order first")
            return
        item = self.item_var.get()
        qty = int(self.qty_entry.get())
        price = self.menu.get_price(item)
        self.order.add_item(item, qty, price)
        self.output.insert("end", f"Added {item} x {qty}\n")

    def pay_order(self):
        if not self.order:
            return
        msg = self.order.process_payment()
        messagebox.showinfo("Payment", msg)

    def show_bill(self):
        if not self.order:
            return
        self.output.insert("end", "\n----- BILL -----\n")
        for item in self.order.items:
            self.output.insert("end", f"{item['name']} x {item['qty']} = ₹{item['total']}\n")
        self.output.insert("end", f"Total: ₹{self.order.total()}\nStatus: {self.order.status}\n\n")
        self.order.save_bill()


# ---------- Run ----------
root = tk.Tk()
app = ModernCanteenGUI(root)
root.mainloop()
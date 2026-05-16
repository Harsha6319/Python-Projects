import customtkinter as ctk
import schedule
import threading
import time
import json
import os
from plyer import notification
# Set the look and feel
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AlertApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Daily Schedule Alerter")
        self.geometry("400x450")

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Daily Schedule Manager", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.task_entry = ctk.CTkEntry(self, placeholder_text="Task Name (e.g., Take Meds)")
        self.task_entry.pack(pady=10, padx=20, fill="x")

        self.time_entry = ctk.CTkEntry(self, placeholder_text="Time (24h format HH:MM)")
        self.time_entry.pack(pady=10, padx=20, fill="x")

        self.add_button = ctk.CTkButton(self, text="Add Alert", command=self.add_alert)
        self.add_button.pack(pady=20)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Active Alerts")
        self.scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Start the background scheduler thread
        threading.Thread(target=self.run_scheduler, daemon=True).start()

    def send_alert(self, task):
        notification.notify(
            title="Schedule Alert",
            message=f"It is time for: {task}",
            timeout=10
        )

    def add_alert(self):
        task = self.task_entry.get()
        alert_time = self.time_entry.get()

        if task and alert_time:
            # Add to schedule logic
            schedule.every().day.at(alert_time).do(self.send_alert, task=task)
            
            # Update UI list
            label = ctk.CTkLabel(self.scrollable_frame, text=f"[{alert_time}] {task}")
            label.pack(anchor="w", padx=10)
            
            # Clear inputs
            self.task_entry.delete(0, 'end')
            self.time_entry.delete(0, 'end')

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(10)

if __name__ == "__main__":
    app = AlertApp()
    app.mainloop()
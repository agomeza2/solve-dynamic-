import tkinter as tk
from tkinter import messagebox

class DataEntryPage:
    def __init__(self, master, button_number):
        self.master = master
        self.button_number = button_number

        self.entry_label = tk.Label(master, text=f"Enter data for Button {button_number}:")
        self.entry_label.pack()

        self.data_entry = tk.Entry(master)
        self.data_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_data)
        self.submit_button.pack()

    def submit_data(self):
        data = self.data_entry.get()
        messagebox.showinfo("Data Submitted", f"Data for Button {self.button_number}: {data}")

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Wellcome to Solve Dynamics")

        self.buttons = []
        for i in range(1, 18):
            button = tk.Button(master, text=f"Button {i}", command=lambda num=i: self.open_data_entry(num))
            button.pack()
            self.buttons.append(button)

    def open_data_entry(self, button_number):
        top = tk.Toplevel(self.master)
        page = DataEntryPage(top, button_number)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()

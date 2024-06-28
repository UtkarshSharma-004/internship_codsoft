import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import re
import json
import os

# Contact Manager Application
class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        self.contacts = {}

        # Creating the UI
        self.create_widgets()
        self.load_contacts()

    def create_widgets(self):
        self.create_menu()
        self.create_contact_list()
        self.create_search_bar()
        self.create_buttons()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

    def create_contact_list(self):
        self.tree = ttk.Treeview(self.root, columns=('Name', 'Phone', 'Email', 'Address'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Address', text='Address')
        self.tree.pack(fill=tk.BOTH, expand=True, pady=20)

    def create_search_bar(self):
        self.search_var = tk.StringVar()
        search_frame = tk.Frame(self.root, bg='#f0f0f0')
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Search", bg='#f0f0f0').pack(side=tk.LEFT, padx=5)
        tk.Entry(search_frame, textvariable=self.search_var).pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_contact).pack(side=tk.LEFT, padx=5)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Contact", command=self.add_contact, bg='#4caf50', fg='white').pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Update Contact", command=self.update_contact, bg='#2196f3', fg='white').pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, bg='#f44336', fg='white').pack(side=tk.LEFT, padx=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")

        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and Phone are required!")
            return

        if not re.match(r'^\d{10}$', phone):
            messagebox.showwarning("Input Error", "Phone number must be 10 digits!")
            return

        if email and not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
            messagebox.showwarning("Input Error", "Email must be a valid Gmail address!")
            return

        self.contacts[phone] = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        self.update_contact_list()
        self.save_contacts()

    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            phone = self.tree.item(selected_item)['values'][1]
            name = simpledialog.askstring("Input", "Enter Name:", initialvalue=self.contacts[phone]['Name'])
            email = simpledialog.askstring("Input", "Enter Email:", initialvalue=self.contacts[phone]['Email'])
            address = simpledialog.askstring("Input", "Enter Address:", initialvalue=self.contacts[phone]['Address'])

            if not name:
                messagebox.showwarning("Input Error", "Name is required!")
                return

            if email and not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
                messagebox.showwarning("Input Error", "Email must be a valid Gmail address!")
                return

            self.contacts[phone]['Name'] = name
            self.contacts[phone]['Email'] = email
            self.contacts[phone]['Address'] = address
            self.update_contact_list()
            self.save_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            phone = self.tree.item(selected_item)['values'][1]
            if phone in self.contacts:
                del self.contacts[phone]
                self.update_contact_list()
                self.save_contacts()
            else:
                messagebox.showerror("Deletion Error", "Selected contact does not exist.")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def search_contact(self):
        search_term = self.search_var.get().lower()
        filtered_contacts = {phone: details for phone, details in self.contacts.items()
                             if search_term in details['Name'].lower() or search_term in phone}
        self.update_contact_list(filtered_contacts)

    def update_contact_list(self, contacts=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        contacts = contacts if contacts else self.contacts
        for phone, details in contacts.items():
            self.tree.insert('', 'end', values=(details['Name'], phone, details['Email'], details['Address']))

    def save_contacts(self):
        with open('contacts.json', 'w') as f:
            json.dump(self.contacts, f)

    def load_contacts(self):
        if os.path.exists('contacts.json'):
            with open('contacts.json', 'r') as f:
                self.contacts = json.load(f)
            self.update_contact_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.create_gui()

    def create_gui(self):
        # Labels
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        tk.Label(self.root, text="Phone:").grid(row=1, column=0)
        tk.Label(self.root, text="Email:").grid(row=2, column=0)
        tk.Label(self.root, text="Address:").grid(row=3, column=0)

        # Entry fields
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1)
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1)
        tk.Entry(self.root, textvariable=self.address_var).grid(row=3, column=1)

        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=9, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        self.clear_entry_fields()
        messagebox.showinfo("Contact Added", "Contact has been added.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("No Contacts", "There are no contacts to display.")

    def search_contact(self):
        keyword = self.name_var.get()

        search_results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower()]
        if search_results:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone}" for contact in search_results])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("No Results", "No contacts found matching the search criteria.")

    def update_contact(self):
        # Implement the update contact functionality here
        pass

    def delete_contact(self):
        # Implement the delete contact functionality here
        pass

    def clear_entry_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set()

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

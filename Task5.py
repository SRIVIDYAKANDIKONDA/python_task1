class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, name, phone_number, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = phone_number
                contact.email = email
                contact.address = address
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[idx]
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")


def main():
    contact_book = ContactBook()
    
    while True:
        print("\n==== Contact Management System ====")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)

        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

class Contact:
    def __init__(self, name, phone_no, email, address):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, data):
        self.contacts.append(data)

    def view_contacts(self):
        print("\nContacts:")
        for i, data in enumerate(self.contacts, start=1):
            print(f"{i}.\nName: {data.name}\nPhone Number: {data.phone_no}\nEmail: {data.email}")


    def search_contact(self, key_item):
        results = [data for data in self.contacts if key_item.lower() in data.name.lower() or key_item in data.phone_no]
        print("\nSearch results:")
        for i, result in enumerate(results, start=1):
            print(f"{i}.\nName: {result.name}\nPhone Number: {result.phone_no}\nEmail: {result.email}")


    def update_contact(self, name):
        for data in self.contacts:
            if data.name.lower() == name.lower():
                new_phone_no = input("Enter the new phone number: ")
                data.phone_no = new_phone_no
                print(f"Contact updated: {data.name}'s new phone number is {data.phone_no}")
                return
        print(f"Contact not found with the name {name}")

    def delete_contact(self, name):
        for data in self.contacts:
            if data.name.lower() == name.lower():
                self.contacts.remove(data)
                print(f"Contact deleted: {data.name}")
                return
        print(f"Contact not found with the name {name}")


if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_no = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_no, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully!")

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            key_item = input("Enter name or phone number to search: ")
            contact_manager.search_contact(key_item)

        elif choice == "4":
            name = input("Enter the name of the data to update: ")
            contact_manager.update_contact(name)

        elif choice == "5":
            name = input("Enter the name of the data to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("**Invalid choice**\nPlease enter a number from 1 to 6.")

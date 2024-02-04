#1task 5

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        contact_info = {
            "phone_number": phone_number,
            "email": email,
            "address": address,
        }
        self.contacts[name] = contact_info
        print(f"Contact {name} added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone_number']}")

    def search_contact(self, keyword):
        results = []
        for name, info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in info['phone_number']:
                results.append((name, info))
        return results

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {
                "phone_number": phone_number,
                "email": email,
                "address": address,
            }
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(keyword)
            if search_results:
                print("\nSearch Results:")
                for name, info in search_results:
                    print(f"Name: {name}, Phone: {info['phone_number']}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(name, phone_number, email, address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()


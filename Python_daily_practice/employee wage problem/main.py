import json
import os

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zip Code: {self.zip_code}\n"
                f"Phone: {self.phone}\n"
                f"Email: {self.email}")

    def __eq__(self, other):
        return (self.first_name == other.first_name and 
                self.last_name == other.last_name)

    def __hash__(self):
        return hash((self.first_name, self.last_name))


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}

    def add_contact(self, contact):
        if (contact.first_name, contact.last_name) in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[(contact.first_name, contact.last_name)] = contact
            print("Contact added.")

    def edit_contact(self, contact_name, updated_contact):
        if contact_name in self.contacts:
            self.contacts[contact_name] = updated_contact
            print("Contact updated.")
        else:
            print("Contact not found.")

    def delete_contact(self, contact_name):
        if contact_name in self.contacts:
            del self.contacts[contact_name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def search_by_city_or_state(self, city, state):
        results = []
        for contact in self.contacts.values():
            if (city and contact.city == city) or (state and contact.state == state):
                results.append(contact)
        return results

    def count_by_city_or_state(self, city, state):
        count = 0
        for contact in self.contacts.values():
            if (city and contact.city == city) or (state and contact.state == state):
                count += 1
        return count

    def save_to_files(self):
        filename = f"{self.name}.json"
        with open(filename, 'w') as f:
            data = [contact.__dict__ for contact in self.contacts.values()]
            json.dump(data, f)

    @staticmethod
    def load_from_files(name):
        filename = f"{name}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                address_book = AddressBook(name)
                for contact_data in data:
                    contact = Contact(**contact_data)
                    address_book.add_contact(contact)
                return address_book
        else:
            return AddressBook(name)


def main():
    address_books = {}
    
    # Load existing address books
    if os.path.exists('address_books.json'):
        with open('address_books.json', 'r') as f:
            book_data = json.load(f)
            for name in book_data:
                address_books[name] = AddressBook.load_from_files(name)

    while True:
        print("\nWelcome to Address Book Program")
        print("1. Create a Contact")
        print("2. Add New Contact")
        print("3. Edit Existing Contact")
        print("4. Delete Contact")
        print("5. Add Multiple Contacts")
        print("6. Manage Multiple Address Books")
        print("7. Prevent Duplicate Entries")
        print("8. Search Contacts by City or State")
        print("9. View Contacts by City or State")
        print("10. Count Contacts by City or State")
        print("11. Save and Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter address book name: ")
            # Check if address book exists, if not create a new one
            if name not in address_books:
                address_books[name] = AddressBook(name)
                print(f"Created new address book: {name}")

            # Add contact to the address book
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
            address_books[name].add_contact(contact)

        elif choice == '2':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found. Creating a new address book.")
                address_books[name] = AddressBook(name)

            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
            address_books[name].add_contact(contact)

        elif choice == '3':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found.")
                continue
            contact_name = tuple(input("Enter contact's first and last name to edit (format: First Last): ").split())
            if len(contact_name) != 2:
                print("Invalid name format.")
                continue
            if contact_name in address_books[name].contacts:
                first_name = input("New First Name: ")
                last_name = input("New Last Name: ")
                address = input("New Address: ")
                city = input("New City: ")
                state = input("New State: ")
                zip_code = input("New Zip Code: ")
                phone = input("New Phone: ")
                email = input("New Email: ")
                updated_contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
                address_books[name].edit_contact(contact_name, updated_contact)
            else:
                print("Contact not found.")

        elif choice == '4':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found.")
                continue
            contact_name = tuple(input("Enter contact's first and last name to delete (format: First Last): ").split())
            if len(contact_name) != 2:
                print("Invalid name format.")
                continue
            address_books[name].delete_contact(contact_name)

        elif choice == '5':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found.")
                continue
            num_contacts = int(input("Enter number of contacts to add: "))
            for _ in range(num_contacts):
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                address = input("Address: ")
                city = input("City: ")
                state = input("State: ")
                zip_code = input("Zip Code: ")
                phone = input("Phone: ")
                email = input("Email: ")
                contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
                address_books[name].add_contact(contact)

        elif choice == '6':
            name = input("Enter address book name to add: ")
            if name not in address_books:
                address_books[name] = AddressBook(name)
                print(f"Created address book: {name}")
            else:
                print("Address book already exists.")

        elif choice == '7':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found.")
                continue
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
            address_books[name].add_contact(contact)

        elif choice == '8':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found.")
                continue
            city = input("Enter city (leave empty if not searching by city): ")
            state = input("Enter state (leave empty if not searching by state): ")
            results = address_books[name].search_by_city_or_state(city, state)
            for contact in results:
                print(contact)

        elif choice == '9':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found.")
                continue
            city = input("Enter city (leave empty if not searching by city): ")
            state = input("Enter state (leave empty if not searching by state): ")
            results = address_books[name].search_by_city_or_state(city, state)
            for contact in results:
                print(contact)

        elif choice == '10':
            name = input("Enter address book name: ")
            if name not in address_books:
                print("Address book not found.")
                continue
            city = input("Enter city (leave empty if not searching by city): ")
            state = input("Enter state (leave empty if not searching by state): ")
            count = address_books[name].count_by_city_or_state(city, state)
            print(f"Count of contacts: {count}")

        elif choice == '11':
            for book_name, address_book in address_books.items():
                address_book.save_to_files()
            with open('address_books.json', 'w') as f:
                json.dump(list(address_books.keys()), f)
            print("Data saved and exiting.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

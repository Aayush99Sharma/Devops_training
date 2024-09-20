import json
import csv
import os

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def to_dict(self):
        return {
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'Address': self.address,
            'City': self.city,
            'State': self.state,
            'Zip Code': self.zip_code,
            'Phone Number': self.phone_number,
            'Email': self.email
        }

# Helper functions to load and save all contacts

def load_contacts_json(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                try:
                    data = json.loads(line.strip())
                    contacts.append(Contact(
                        first_name=data.get('First Name', ''),
                        last_name=data.get('Last Name', ''),
                        address=data.get('Address', ''),
                        city=data.get('City', ''),
                        state=data.get('State', ''),
                        zip_code=str(data.get('Zip Code', '')),
                        phone_number=str(data.get('Phone Number', '')),
                        email=data.get('Email', '')
                    ))
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                except TypeError as e:
                    print(f"Error initializing Contact object: {e}")
    return contacts


def save_contacts_json(contacts, filename):
    with open(filename, 'w') as file:
        for contact in contacts:
            json.dump(contact.to_dict(), file)
            file.write('\n')

def load_contacts_csv(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact_data = {
                    'first_name': row.get('First Name', ''),
                    'last_name': row.get('Last Name', ''),
                    'address': row.get('Address', ''),
                    'city': row.get('City', ''),
                    'state': row.get('State', ''),
                    'zip_code': row.get('Zip Code', ''),
                    'phone_number': row.get('Phone Number', ''),
                    'email': row.get('Email', '')
                }
                contacts.append(Contact(**contact_data))
    return contacts


def save_contacts_csv(contacts, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=contacts[0].to_dict().keys())
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact.to_dict())

def save_contacts_txt(contacts, filename):
    # Rewrite the entire contacts.txt file
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"First Name: {contact.first_name}\n")
            file.write(f"Last Name: {contact.last_name}\n")
            file.write(f"Address: {contact.address}\n")
            file.write(f"City: {contact.city}\n")
            file.write(f"State: {contact.state}\n")
            file.write(f"Zip Code: {contact.zip_code}\n")
            file.write(f"Phone Number: {contact.phone_number}\n")
            file.write(f"Email: {contact.email}\n")
            file.write("\n")  # Add a blank line between contacts

def save_as_txt(contact, filename):
    with open(filename, 'a') as file:
        file.write(f"First Name: {contact.first_name}\n")
        file.write(f"Last Name: {contact.last_name}\n")
        file.write(f"Address: {contact.address}\n")
        file.write(f"City: {contact.city}\n")
        file.write(f"State: {contact.state}\n")
        file.write(f"Zip Code: {contact.zip_code}\n")
        file.write(f"Phone Number: {contact.phone_number}\n")
        file.write(f"Email: {contact.email}\n")
        file.write("\n")  # Add a blank line after each contact

def display_txt(filename):
    print("\n--- Contacts in TXT Format ---")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No contacts found in TXT format.")

def display_json(filename):
    print("\n--- Contacts in JSON Format ---")
    try:
        contacts = load_contacts_json(filename)
        for contact in contacts:
            print(json.dumps(contact.to_dict(), indent=4))
    except FileNotFoundError:
        print("No contacts found in JSON format.")

def display_csv(filename):
    print("\n--- Contacts in CSV Format ---")
    try:
        contacts = load_contacts_csv(filename)
        for contact in contacts:
            print(contact.to_dict())
    except FileNotFoundError:
        print("No contacts found in CSV format.")

# New functions for edit, delete, and update contacts

def edit_contact(contacts, first_name, last_name):
    first_name = first_name.strip().lower()  # Trim and convert to lowercase
    last_name = last_name.strip().lower()    # Trim and convert to lowercase

    for contact in contacts:
        # Convert stored names to lowercase for case-insensitive comparison
        if contact.first_name.strip().lower() == first_name and contact.last_name.strip().lower() == last_name:
            print(f"Editing contact: {contact.to_dict()}")
            contact.first_name = input(f"First Name [{contact.first_name}]: ") or contact.first_name
            contact.last_name = input(f"Last Name [{contact.last_name}]: ") or contact.last_name
            contact.address = input(f"Address [{contact.address}]: ") or contact.address
            contact.city = input(f"City [{contact.city}]: ") or contact.city
            contact.state = input(f"State [{contact.state}]: ") or contact.state
            contact.zip_code = input(f"Zip Code [{contact.zip_code}]: ") or contact.zip_code
            contact.phone_number = input(f"Phone Number [{contact.phone_number}]: ") or contact.phone_number
            contact.email = input(f"Email [{contact.email}]: ") or contact.email
            print("Contact updated.")
            return True  # Return True when contact is edited successfully
    print("Contact not found.")
    return False  # Return False when contact is not found


def delete_contact(contacts, first_name, last_name):
    first_name = first_name.strip().lower()  # Case-insensitive comparison
    last_name = last_name.strip().lower()

    for contact in contacts:
        if contact.first_name.strip().lower() == first_name and contact.last_name.strip().lower() == last_name:
            contacts.remove(contact)
            print(f"Contact {first_name} {last_name} deleted.")
            return contacts  # Return the modified list
    print("Contact not found.")
    return contacts  # Return the original list if not found

def main():
    while True:
        print("\n1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter choice: ")

        match choice:
            case '1':
                # Add contact logic remains the same
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                address = input("Address: ")
                city = input("City: ")
                state = input("State: ")
                zip_code = input("Zip Code: ")
                phone_number = input("Phone Number: ")
                email = input("Email: ")

                contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                
                # Save contact in different formats
                save_as_txt(contact, 'contacts.txt')
                contacts = load_contacts_json('contacts.json')
                contacts.append(contact)
                save_contacts_json(contacts, 'contacts.json')
                
                contacts = load_contacts_csv('contacts.csv')
                contacts.append(contact)
                save_contacts_csv(contacts, 'contacts.csv')

                print("Contact saved.")
            
            case '2':
                # Display contact logic remains the same
                print("1. Display TXT")
                print("2. Display JSON")
                print("3. Display CSV")
                display_choice = input("Enter choice: ")

                match display_choice:
                    case '1':
                        display_txt('contacts.txt')
                    case '2':
                        display_json('contacts.json')
                    case '3':
                        display_csv('contacts.csv')
                    case _:
                        print("Invalid choice. Please try again.")
            
            case '3':
                # Edit contact logic: save contacts back after editing
                first_name = input("Enter the first name of the contact to edit: ")
                last_name = input("Enter the last name of the contact to edit: ")

                contacts = load_contacts_json('contacts.json')
                if edit_contact(contacts, first_name, last_name):
                    save_contacts_json(contacts, 'contacts.json')
                    save_contacts_csv(contacts, 'contacts.csv')
                    save_contacts_txt(contacts, 'contacts.txt')  # Update TXT file too
                else:
                    print("Contact not found.")
            
            case '4':
                # Delete contact logic: save contacts back after deletion
                first_name = input("Enter the first name of the contact to delete: ")
                last_name = input("Enter the last name of the contact to delete: ")

                contacts = load_contacts_json('contacts.json')
                contacts = delete_contact(contacts, first_name, last_name)  # Get the modified list
                if contacts:  # Check if the contacts list is not empty
                    save_contacts_json(contacts, 'contacts.json')
                    save_contacts_csv(contacts, 'contacts.csv')
                    save_contacts_txt(contacts, 'contacts.txt')  # Update TXT file too
                else:
                    # If contacts list is empty, just delete the files or handle accordingly
                    os.remove('contacts.json')
                    os.remove('contacts.csv')
                    os.remove('contacts.txt')
                    print("All contacts deleted. Files removed.")

            case '5':
                print("Exiting program.")
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

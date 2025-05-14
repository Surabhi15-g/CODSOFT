# Contact Management System

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"Contact '{name}' added successfully.\n")

def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print(f"   Address: {contact['address']}\n")

def search_contacts(contacts):
    """Search contacts by name or phone number."""
    query = input("Enter name or phone to search: ").strip().lower()
    results = []
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone'].lower():
            results.append(contact)
    if results:
        print(f"\nFound {len(results)} contact(s):")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No matching contacts found.\n")

def update_contact(contacts):
    """Update contact details."""
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the contact number to update: "))
        if 1 <= index <= len(contacts):
            contact = contacts[index - 1]
            print(f"Updating contact '{contact['name']}'")
            new_name = input(f"Enter new name (leave blank to keep '{contact['name']}'): ").strip()
            new_phone = input(f"Enter new phone (leave blank to keep '{contact['phone']}'): ").strip()
            new_email = input(f"Enter new email (leave blank to keep '{contact['email']}'): ").strip()
            new_address = input(f"Enter new address (leave blank to keep '{contact['address']}'): ").strip()

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print("Contact updated successfully.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_contact(contacts):
    """Delete a contact."""
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the contact number to delete: "))
        if 1 <= index <= len(contacts):
            removed = contacts.pop(index - 1)
            print(f"Contact '{removed['name']}' deleted successfully.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    contacts = []

    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
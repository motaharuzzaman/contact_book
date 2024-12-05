def search_contact(all_contacts):
    if not all_contacts:
        print("No contacts available to search.")
        return

    phone_number = input("Enter Phone Number to search: ")

    # Search for the contact with the given phone_number
    for contact in all_contacts:
        if contact["phone_number"] == phone_number:
            print(f"Name: {contact['name']} | Email: {contact['email']} | Phone Number: {contact['phone_number']} | Address: {contact['address']}")
            return

    print("Contact not found.")
from save_all_contacts import save_all_contacts

def remove_contact(all_contacts):
    if not all_contacts:
        print("No contacts available to remove.")
        return all_contacts

    phone_number = input("Enter Phone Number to remove: ")

    # Search for the contact with the given phone_number
    for contact in all_contacts:
        if contact["phone_number"] == phone_number:
            all_contacts.remove(contact)
            save_all_contacts(all_contacts)  # Update the CSV file
            print("Contact removed successfully.")
            return all_contacts

    print("Contact not found.")
    return all_contacts

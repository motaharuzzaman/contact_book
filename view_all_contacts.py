def view_all_contacts(all_contacts):
    if all_contacts:
        for contact in all_contacts:
            print(f"Name: {contact['name']} | Email: {contact['email']} | Phone Number: {contact['phone_number']} | Address: {contact['address']}")
    else:
        print("No Contacts Found")
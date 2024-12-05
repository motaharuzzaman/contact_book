from save_all_contacts import save_all_contacts

def add_contact(all_contacts):
    name = input("Enter Name: ")
    email = input("Enter Email Address: ")

    phone_number = input("Enter Phone Number: ")
    for contact in all_contacts:
        if contact["phone_number"] == phone_number:
            print("Phone Number already exists.")
            return all_contacts  # Return without adding duplicate

    address = input("Enter Address: ")

    contact = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "address": address,
    }

    all_contacts.append(contact)
    save_all_contacts(all_contacts)

    print("Contact Added Successfully")
    return all_contacts
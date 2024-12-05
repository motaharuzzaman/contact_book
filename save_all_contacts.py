import os

def save_all_contacts(all_contacts):
    with open("all_contacts.csv", "w") as fp:
        for contact in all_contacts:
            line = f"{contact['name']},{contact['email']},{contact['phone_number']},{contact['address']}\n"
            fp.write(line)

def load_all_contacts():
    all_contacts = []
    if not os.path.exists("all_contacts.csv"):
        return all_contacts  # Return empty list if file does not exist

    with open("all_contacts.csv", "r") as fp:
        for line in fp:
            # Strip whitespace and skip empty or malformed lines
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 4:  # Ensure there are exactly 4 fields
                print(f"Skipping malformed line: {line}")
                continue

            name, email, phone_number, address = parts
            contact = {
                "name": name.strip(),
                "email": email.strip(),
                "phone_number": phone_number.strip(),
                "address": address.strip(),
            }
            all_contacts.append(contact)

    return all_contacts
import add_contact
import view_all_contacts
import search_contact
import remove_contact  # Import the new remove contact module
from save_all_contacts import load_all_contacts

# Load existing contacts from the CSV file
all_contacts = load_all_contacts()

while True:
    print("\nWelcome to the Contact Management System")
    print("0. Exit")
    print("1. Add a Contact")
    print("2. Search a Contact")
    print("3. View all Contacts")
    print("4. Remove a Contact")

    option = input("Enter an option: ")

    if option == "0":
        print("Thanks for using Contact Management System")
        break

    elif option == "1":
        all_contacts = add_contact.add_contact(all_contacts)

    elif option == "2":
        search_contact.search_contact(all_contacts)

    elif option == "3":
        view_all_contacts.view_all_contacts(all_contacts)

    elif option == "4":
        all_contacts = remove_contact.remove_contact(all_contacts)

    else:
        print("Please Choose a Valid Option")

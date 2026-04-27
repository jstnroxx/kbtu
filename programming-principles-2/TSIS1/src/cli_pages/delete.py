from src import phonebook

from src.utility import clearLog
from src.cli_pages import invalid, response

def view():
    clearLog()
    print("=" * 50)
    print("    TSIS Phonebook Delete")
    print("=" * 50)
    print("Commands:")
    print("    1 - Delete contact by name")
    print("    2 - Delete contact by phone")
    print("    re - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
        
    if command == "re":
        clearLog()
        return
    elif command == "1":
        name = input("\nEnter contact name to delete: ").strip()
        
        output = phonebook.deleteContactByName(name)
        
        if output == True:
            response.view("Delete", "Successfully deleted contact.")
        else:
            response.view("Delete", output)
    elif command == "2":
        phone = input("\nEnter contact phone number to delete: ").strip()
        
        output = phonebook.deleteContactByPhone(phone)
        
        if output == True:
            response.view("Delete", "Successfully deleted contact.")
        else:
            response.view("Delete", output)
    else:
        invalid.view()
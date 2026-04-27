from src import phonebook

from src.utility import clearLog
from src.cli_pages import invalid, response

def view():
    clearLog()
    print("=" * 50)
    print("    TSIS Phonebook Modify")
    print("=" * 50)
    print("Commands:")
    print("    1 - Update contact name")
    print("    re - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
        
    if command == "re":
        clearLog()
        return
    elif command == "1":
        oldName = input("\nEnter contact name to update: ").strip()
        newName = input("Enter new contact name: ").strip()
        
        output = phonebook.updateContact(oldName, newName)
        
        if output == True:
            response.view("Modify", "Successfully updated contact.")
        else:
            response.view("Modify", output)
    else:
        invalid.view()
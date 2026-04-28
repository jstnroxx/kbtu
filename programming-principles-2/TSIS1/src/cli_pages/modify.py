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
    print("    2 - Add new contact phone")
    print("    3 - Update contact group")
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
    elif command == "2":
        name = input("\nEnter contact name to add phone: ").strip()
        newPhone = input("Enter new phone number: ").strip()
        newType = input("Enter phone type (home, work, mobile): ").strip()
        
        output = phonebook.addPhone(name, newPhone, newType)
        
        if output == True:
            response.view("Modify", "Successfully updated contact phones.")
        else:
            response.view("Modify", output)
    elif command == "3":
        name = input("\nEnter contact name to move group: ").strip()
        newGroup = input("Enter group to move contact into: ").strip()
        
        output = phonebook.moveGroup(name, newGroup)
        
        if output == True:
            response.view("Modify", "Successfully moved contact.")
        else:
            response.view("Modify", output)      
    else:
        invalid.view()
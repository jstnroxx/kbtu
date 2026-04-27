from src import phonebook

from src.utility import clearLog
from src.cli_pages import invalid, response

def view():
    clearLog()
    print("=" * 50)
    print("    TSIS Phonebook Insert")
    print("=" * 50)
    print("Commands:")
    print("    1 - Insert contact manually")
    print("    re - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
        
    if command == "re":
        clearLog()
        return
    elif command == "1":
        group = input("\nGroup name: ").strip()
        name = input("Contact name: ").strip()
        email = input("Contact email: ").strip()
        birthday = input("Contact birthday (YYYY-MM-DD):").strip()
        phone = input("Phone number: ").strip()
        phoneType = input("Phone type (home, work, mobile): ").strip()
        
        output = phonebook.insertContact(group, name, email, birthday, phone, phoneType)
        
        if output == True:
            response.view("Insert", "Successfully inserted contact.")
        else:
            response.view("Insert", output)
    else:
        invalid.view()
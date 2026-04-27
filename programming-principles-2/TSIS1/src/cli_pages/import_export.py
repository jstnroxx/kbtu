from src import phonebook

from src.utility import clearLog
from src.cli_pages import invalid, response

def view():
    clearLog()
    print("=" * 50)
    print("    TSIS Phonebook Import/Export")
    print("=" * 50)
    print("Commands:")
    print("    1 - Import from contacts.csv")
    print("    2 - Import from contacts.json")
    print("    3 - Export to contacts.json")
    print("    re - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
        
    if command == "re":
        clearLog()
        return
    elif command == "1":
        output = phonebook.importCsv()
        
        if output == True:
            response.view("Import/Export", "Successfully imported contacts from contacts.csv")
        else:
            response.view("Import/Export", output)
    elif command == "2":
        output = phonebook.importJson()
        
        if output == True:
            response.view("Import/Export", "Successfully imported contacts from contacts.json")
        else:
            response.view("Import/Export", output)
    elif command == "3":
        output = phonebook.exportJson()
        
        if output == True:
            response.view("Import/Export", "Successfully exported contacts to contacts.json")
        else:
            response.view("Import/Export", output)
    else:
        invalid.view()
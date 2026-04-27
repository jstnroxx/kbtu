from src import phonebook

from src.utility import clearLog
from src.cli_pages import invalid, response

def view():
    clearLog()
    print("=" * 50)
    print("    TSIS Phonebook Search")
    print("=" * 50)
    print("Commands:")
    print("    1 - Search contacts by name")
    print("    2 - Search contacts by phone prefix")
    print("    3 - Search contacts by pattern")
    print("    re - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
        
    if command == "re":
        clearLog()
        return
    elif command == "1":
        name = input("\nEnter name: ").strip()
        
        output = phonebook.searchByName(name)
        
        formatted = ""
        
        if type(output) == type("abc"):    
            formatted = output
        elif len(output) > 0:
            formatted = "\n".join(str(row) for row in output)
        else:
            formatted = "No data found."
        
        response.view("Search", formatted)
    elif command == "2":
        phone = input("\nEnter phone prefix: ").strip()
        
        output = phonebook.searchByPhone(phone)
        
        formatted = ""
        
        if type(output) == type("abc"):    
            formatted = output
        elif len(output) > 0:
            formatted = "\n".join(str(row) for row in output)
        else:
            formatted = "No data found."
        
        response.view("Search", formatted)
    elif command == "3":
        pattern = input("\nEnter pattern: ").strip()
        
        output = phonebook.searchByPattern(pattern)
        
        formatted = ""
        
        if type(output) == type("abc"):    
            formatted = output
        elif len(output) > 0:
            formatted = "\n".join(str(row) for row in output)
        else:
            formatted = "No data found."
        
        response.view("Search", formatted)
    else:
        invalid.view()
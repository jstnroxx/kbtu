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
    print("    4 - Get all contacts paginated")
    print("    re - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
        
    if command == "re":
        clearLog()
        return
    elif command == "1":
        name = input("\nEnter name: ").strip()
        
        groupFilter = input("Filter group?: ").strip()
        sortBy = input("Sort by? (name, birthday): ").strip().lower()
        sortType = input("Sort type? (asc, desc): ").strip().lower()
        
        output = phonebook.searchByName(name)
        
        formatted = ""
        
        if type(output) == type("abc"):    
            formatted = output
        elif len(output) > 0:
            if groupFilter:
                output = list(filter(lambda tple : tple[2] == groupFilter, output))
                
            if sortBy == "name":
                output.sort(key = lambda tple : tple[0], reverse = True if sortType == "desc" else False)
            elif sortBy == "birthday":
                output.sort(key = lambda tple : tple[1], reverse = True if sortType == "desc" else False)
            
            formatted = "\n".join(str(row) for row in output)
        else:
            formatted = "No data found."
        
        response.view("Search", formatted)
    elif command == "2":
        phone = input("\nEnter phone prefix: ").strip()
        
        groupFilter = input("Filter group?: ").strip()
        sortBy = input("Sort by? (name, birthday): ").strip().lower()
        sortType = input("Sort type? (asc, desc): ").strip().lower()
        
        output = phonebook.searchByPhone(phone)
        
        formatted = ""
        
        if type(output) == type("abc"):    
            formatted = output
        elif len(output) > 0:
            if groupFilter:
                output = list(filter(lambda tple : tple[2] == groupFilter, output))
                
            if sortBy == "name":
                output.sort(key = lambda tple : tple[0], reverse = True if sortType == "desc" else False)
            elif sortBy == "birthday":
                output.sort(key = lambda tple : tple[1], reverse = True if sortType == "desc" else False)
            
            formatted = "\n".join(str(row) for row in output)
        else:
            formatted = "No data found."
        
        response.view("Search", formatted)
    elif command == "3":
        pattern = input("\nEnter pattern: ").strip()
        
        groupFilter = input("Filter group?: ").strip()
        sortBy = input("Sort by? (name, birthday): ").strip().lower()
        sortType = input("Sort type? (asc, desc): ").strip().lower()
        
        output = phonebook.searchByPattern(pattern)
        
        formatted = ""
        
        if type(output) == type("abc"):    
            formatted = output
        elif len(output) > 0:
            if groupFilter:
                output = list(filter(lambda tple : tple[2] == groupFilter, output))
                
            if sortBy == "name":
                output.sort(key = lambda tple : tple[0], reverse = True if sortType == "desc" else False)
            elif sortBy == "birthday":
                output.sort(key = lambda tple : tple[1], reverse = True if sortType == "desc" else False)
            
            formatted = "\n".join(str(row) for row in output)
        else:
            formatted = "No data found."
        
        response.view("Search", formatted)
    elif command == "4":
        offset = 0
        
        groupFilter = input("\nFilter group?: ").strip()
        sortBy = input("Sort by? (name, birthday): ").strip().lower()
        sortType = input("Sort type? (asc, desc): ").strip().lower()
        
        while True:
            output = phonebook.getPaginatedContacts(offset, groupFilter, sortBy, sortType)
             
            formatted = ""
        
            if type(output) == type("abc"):    
                formatted = output
            elif len(output) > 0:
                formatted = "\n".join(str(row) for row in output)
            else:
                formatted = "No data found."
            
            clearLog()
            print("=" * 50)
            print(f"    TSIS Phonebook Search (Page {int(offset / 10) + 1})")
            print("=" * 50)
            print(formatted)
            print("=" * 50)
            
            if len(output) == 10:
                print("    next - Next page")
            
            if offset != 0:
                print("    prev - Previous page")
            
            print("    quit - Return")
            print("=" * 50)
            
            command = input("Enter command: ").strip().lower()
            
            if command == "quit":
                clearLog()
                return
            elif command == "next":
                if len(output) == 10: offset += 10
            elif command == "prev":
                if offset - 10 >= 0: offset -= 10
    else:
        invalid.view()
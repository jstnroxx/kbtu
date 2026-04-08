from src import phonebook
from src.cli_pages import home, invalid
from src.utility import clearLog
        
# Main CLI loop
def main():
    while True:
        home.view()
        
        command = input("Enter command: ").strip().lower()
        
        if command == "ex":
            clearLog()
            break
        elif command == "1":
            pass
        elif command == "2":
            pass
        elif command == "3":
            pass
        elif command == "4":
            pass
        elif command == "5":
            pass
        else:
            invalid.view()

# Validate the schema creation and run the CLI
if __name__ == "__main__":
    status = phonebook.createSchema()
    
    if status is True:
        main()
    else:
        print(status)
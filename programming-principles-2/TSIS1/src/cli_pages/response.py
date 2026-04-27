from src.utility import clearLog

def view(header, message):
    clearLog()
    print("=" * 50)
    print("    TSIS Phonebook " + header)
    print("=" * 50)
    print(message)
    print("=" * 50)
    
    input("Press Enter to continue... ")
        
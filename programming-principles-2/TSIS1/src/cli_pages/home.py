from ..utility import clearLog

def view():
    clearLog()
    print("=" * 50)
    print("    TSIS Phonebook")
    print("=" * 50)
    print("Commands:")
    print("    1 - Search contacts")
    print("    2 - Modify contacts")
    print("    3 - Insert contacts")
    print("    4 - Delete contacts")
    print("    5 - Import/export contacts")
    print("    ex - Exit")
    print("=" * 50)
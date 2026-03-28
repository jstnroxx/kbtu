import os
import csv
from initializepb import initPhonebook, initTestPhones
import queries

def clearLog():
    os.system("cls")
    
def homePage():
    clearLog()
    print("=" * 50)
    print("    Phonebook")
    print("=" * 50)
    print("Commands:")
    print("    1 - Insert contacts")
    print("    2 - Modify contacts")
    print("    3 - Query contacts")
    print("    4 - Delete contacts")
    print("    ex - Exit")
    print("=" * 50)
    
def insertPage():
    clearLog()
    print("=" * 50)
    print("    Phonebook Insertion")
    print("=" * 50)
    print("    1 - Import from contacts.csv")
    print("    2 - Create sample contacts")
    print("    3 - Manual insertion")
    print("    ex - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
    
    if command == "ex":
        return
    elif command == "1":
        clearLog()
        print("=" * 50)
        print("    Phonebook Insertion")
        print("=" * 50)
        
        if os.path.exists("contacts.csv"):
            with open("contacts.csv", encoding = "utf-8") as contacts:
                csvReader = csv.reader(contacts)
                
                print(queries.insertManyRows(list(csvReader)))
        else:
            print("No contacts.csv found.")
        
        print("=" * 50)
        input("Press Enter to return to the home page... ")
    elif command == "2":
        clearLog()
        print("=" * 50)
        print("    Phonebook Insertion")
        print("=" * 50)
        print(" How many test contacts to create?")
        print("=" * 50)
        
        amount = input("(0-9999): ").strip()
        
        try:
            amount = int(amount)
        except:
            amount = 1
            
        clearLog()
        print("=" * 50)
        print("    Phonebook Insertion")
        print("=" * 50)
        
        print(initTestPhones(amount))
        
        print("=" * 50)
        input("Press Enter to return to the home page... ")
    elif command == "3":
        clearLog()
        print("=" * 50)
        print("    Phonebook Insertion")
        print("=" * 50)
        
        fname = input("Contacts' first name: ").strip()
        lname = input("Contacts' last name: ").strip()
        phone = input("Contacts' phone number: ").strip()
        
        clearLog()
        print("=" * 50)
        print("    Phonebook Insertion")
        print("=" * 50)
        
        print(queries.upsertRow((fname, lname, phone)))
        
        print("=" * 50)
        input("Press Enter to return to the home page... ")
    else:
        invalidPage()

def modifyPage():
    clearLog()
    print("=" * 50)
    print("    Phonebook Modification")
    print("=" * 50)
    
    contactId = input("Id?: ").strip()
        
    try:
        contactId = int(contactId)
    except:
        contactId = 0
    
    fname = input("First name?: ").strip()
    lname = input("Last name?: ").strip()
    phone = input("Phone number?: ").strip()
        
    newPhone = input("Enter new phone number: ").strip()
    
    clearLog()
    print("=" * 50)
    print("    Phonebook Modification")
    print("=" * 50)
    print(queries.updatePhone(contactId, fname, lname, phone, newPhone))
    print("=" * 50)
    input("Press Enter to return to the home page... ")

def queryPage():
    clearLog()
    print("=" * 50)
    print("    Phonebook Query")
    print("=" * 50)
    print("    1 - Search pattern")
    print("    2 - Search specific")
    print("    ex - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
    
    if command == "1":
        clearLog()
        print("=" * 50)
        print("    Phonebook Query")
        print("=" * 50)
        
        pattern = input("Enter pattern: ").strip()
        
        PAGE_SIZE = 10
        offset = 0
        rows = queries.searchPattern(pattern, offset, PAGE_SIZE)
        
        while len(rows) > 0 and type(rows) != type("abc"):
            clearLog()
            print("=" * 50)
            print(f"    Phonebook Query (Page {(offset // PAGE_SIZE) + 1})")
            print("=" * 50)
            
            for row in rows:
                print(row)
        
            print("=" * 50)
        
            if len(rows) == PAGE_SIZE: 
                print("    Enter - Next page")
                print("    ex - Return")
                print("=" * 50)
            else:
                input("Press Enter to return to the home page... ")
                return
            
            
            command = input("Enter command: ").strip().lower()
            
            if len(rows) == PAGE_SIZE and command == "":
                offset += PAGE_SIZE
                rows = queries.searchPattern(pattern, offset, PAGE_SIZE)
            elif command == "ex":
                return
            else:
                invalidPage()
                
        clearLog()
        print("=" * 50)
        print("    Phonebook Query")
        print("=" * 50)
            
        if type(rows) == type("abc"):
            print(rows)
        elif offset > 0:
            print("End of data.")
        else:
            print("No contacts found.")
            
        print("=" * 50)
        input("Press Enter to return to the home page... ")
    elif command == "2":
        clearLog()
        print("=" * 50)
        print("    Phonebook Query")
        print("=" * 50)
        
        fname = input("First name?: ").strip()
        lname = input("Last name?: ").strip()
        sort = input("Sort? (asc/desc): ").strip().lower() == "desc"
        
        clearLog()
        print("=" * 50)
        print("    Phonebook Query")
        print("=" * 50)
        
        rows = queries.queryRows(fname, lname, sort)
        
        if rows:
            if type(rows) == type("abc"):
                print(rows)
            else:
                for row in rows:
                    print(row)
        else:
            print("No contacts found.")
            
        print("=" * 50)
        input("Press Enter to return to the home page... ")
    elif command == "ex":
        return
    else:
        invalidPage()
    
def deletePage():
    clearLog()
    print("=" * 50)
    print("    Phonebook Deletion")
    print("=" * 50)
    print("    1 - Delete a contact")
    print("    2 - Clear the contact list")
    print("    ex - Return")
    print("=" * 50)
    
    command = input("Enter command: ").strip().lower()
    
    if command == "1":
        clearLog()
        print("=" * 50)
        print("    Phonebook Deletion")
        print("=" * 50)
        
        contactId = input("Id?: ").strip()
        
        try:
            contactId = int(contactId)
        except:
            contactId = 0
        
        fname = input("First name?: ").strip()
        lname = input("Last name?: ").strip()
        phone = input("Phone number?: ").strip()
        
        clearLog()
        print("=" * 50)
        print("    Phonebook Deletion")
        print("=" * 50)
        print(queries.deleteRow(contactId, fname, lname, phone))
        print("=" * 50)
        input("Press Enter to return to the home page... ")
    elif command == "2":
        clearLog()
        print("=" * 50)
        print("    Phonebook Deletion")
        print("=" * 50)
        print(queries.clearTable())
        print("=" * 50)
        input("Press Enter to return to the home page... ")
    elif command == "ex":
        return
    else:
        invalidPage()
    
def invalidPage():
    clearLog()
    print("=" * 50)
    print("    Phonebook")
    print("=" * 50)
    print("Invalid command entered.")
    print("=" * 50)
    input("Press Enter to continue... ")
        
def main():
    while True:
        homePage()
        
        command = input("Enter command: ").strip().lower()
        
        if command == "ex":
            clearLog()
            break
        elif command == "1":
           insertPage()
        elif command == "2":
            modifyPage()
        elif command == "3":
            queryPage()
        elif command == "4":
            deletePage()
        else:
            invalidPage()

if __name__ == "__main__":
    if initPhonebook():
        main()
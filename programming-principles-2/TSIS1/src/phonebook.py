import csv
import json

from pathlib import Path
from psycopg2.extras import RealDictCursor

from .connect import connect


rootFolderPath = Path(__file__).parent.parent 
sqlFolderPath = rootFolderPath / "sql"

# Utilities
def readFromSQL(filename, tag = ""):
    try:
        sqlFilePath = sqlFolderPath / filename
        
        with sqlFilePath.open("r") as file:
            content = file.read()
            
        if tag != "":
            parts = content.split("--@")
            
            for part in parts:
                if part == "":
                    continue
                elif part.split(None, maxsplit = 1)[0] == tag:
                    return part[len(tag):].strip()
                
            return None
        else:
            return content
            
    except Exception as Exc:
        print(Exc)
        
# Database interaction
def createSchema():    
    try:
        global connection
        connection = connect()
        
        with connection.cursor() as cursor:
            cursor.execute(readFromSQL("schema.sql"))
            
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
            
def importCsv():
    try:
        global connection
        connection = connect()
        
        with connection.cursor() as cursor:
            contactsCsvPath = rootFolderPath / "contacts.csv"
            
            if contactsCsvPath.is_file():
                with contactsCsvPath.open("r", encoding = "utf-8") as file:
                    csvReader = csv.reader(file)
  
                    for row in list(csvReader):
                        cursor.execute(readFromSQL("procedures.sql", "createContact"), {
                            'groupName': row[0],
                            'contactName': row[1],
                            'email': row[2],
                            'birthday': row[3],
                            'phone': row[4],
                            'phoneType': row[5]
                        })
            else:
                return "No contacts.csv found in the root folder."
                    
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
            
def importJson():
    try:
        global connection
        connection = connect()
        
        with connection.cursor() as cursor:
            contactsJsonPath = rootFolderPath / "contacts.json"
            
            if contactsJsonPath.is_file():
                with contactsJsonPath.open("r", encoding = "utf-8") as file:
                    contacts = json.load(file)
                    
                for contact in contacts:
                    name = contact["name"]
                    
                    cursor.execute("SELECT id FROM contacts WHERE name = %s", (name,))
                    existence = cursor.fetchone()
                    
                    if existence:
                        action = input(f"'{name}' already exists. Overwrite(o) or skip(s): ").strip().lower()
                        
                        if action != "o":
                            continue
                        
                        cursor.execute("DELETE FROM contacts WHERE id = %s", (existence[0],))
                        
                    group_id = None
                    if contact.get('group_name'):
                        cursor.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name RETURNING id", (contact['group_name'],))
                        group_id = cursor.fetchone()[0]

                    cursor.execute(
                        "INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
                        (name, contact.get('email'), contact.get('birthday'), group_id)
                    )
                    contact_id = cursor.fetchone()[0]

                    if contact.get('phones'):
                        for p in contact['phones']:
                            cursor.execute(
                                "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                                (contact_id, p['phone'], p['type'])
                            )
            else:
                return "No contacts.json found in the root folder."
                    
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
            
def exportJson():
    try:
        global connection
        connection = connect()
        
        with connection.cursor(cursor_factory = RealDictCursor) as cursor:
            cursor.execute(readFromSQL("procedures.sql", "exportJson"))
            
            data = cursor.fetchall()

            with open("contacts.json", 'w') as file:
                json.dump(data, file, indent = 4)
                    
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
            
def insertContact(groupName, contactName, email, birthday, phone, phoneType):
    try:
        global connection
        connection = connect()
        
        if (groupName and contactName and email and birthday and phone and phoneType):
            with connection.cursor() as cursor:
                cursor.execute(readFromSQL("procedures.sql", "createContact"), {
                    'groupName': groupName,
                    'contactName': contactName,
                    'email': email,
                    'birthday': birthday,
                    'phone': phone,
                    'phoneType': phoneType
                })
        else:
            return "Please provide all fields."
                    
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
            
def updateContact(oldName, newName):
    try:
        global connection
        connection = connect()
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM contacts WHERE name = %s", (oldName,))
            existence = cursor.fetchone()
            
            if existence:
                cursor.execute(readFromSQL("procedures.sql", "updateContact"), (newName, existence))
            else:
                return "No contact with such name found."
                    
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
            
def deleteContactByName(name):
    try:
        global connection
        connection = connect()
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM contacts WHERE name = %s", (name,))
            existence = cursor.fetchone()
            
            if existence:
                cursor.execute(readFromSQL("procedures.sql", "deleteContactByName"), (existence,))
            else:
                return "No contact with such name found."
                    
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
            
def deleteContactByPhone(phone):
    try:
        global connection
        connection = connect()
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM phones WHERE phone = %s", (phone,))
            existence = cursor.fetchone()
            
            if existence:
                cursor.execute(readFromSQL("procedures.sql", "deleteContactByPhone"), (existence,))
            else:
                return "No contact with such phone found."
                    
        connection.commit()
        connection.close()
        
        return True
            
    except Exception as Err:
        return Err
        
    finally:
        if connection:
            connection.close()
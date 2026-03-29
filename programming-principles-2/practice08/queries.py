from connect import connect

def resetSerial():
    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute("SELECT MAX(userid) FROM users;")
        lastid = cursor.fetchone()[0] or 0
        cursor.execute(f"ALTER SEQUENCE users_userid_seq RESTART WITH {lastid + 1};")
        
        connection.commit()    
        
        cursor.close()
        connection.close()
    except: 
        print(Exception)

def clearTable():
    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute("DELETE FROM users;")
        resetSerial()
        
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return "Cleared the contact list successfully."
    except Exception as exc:
        return "Something went wrong when clearing the table:\n" + str(exc)

def upsertRow(row):
    command = """
        CREATE OR REPLACE PROCEDURE upsertContact(fname VARCHAR, lname VARCHAR, phoneNum VARCHAR)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM users WHERE firstname = fname AND lastname = lname) THEN
                UPDATE users SET phone = phoneNum WHERE firstname = fname AND lastname = lname;
            ELSE
                INSERT INTO users(firstname, lastname, phone) VALUES(fname, lname, phoneNum);
            END IF;
        END;
        $$;
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        resetSerial()
        cursor.execute(command)
        cursor.execute("CALL upsertContact(%s, %s, %s)", (row[0], row[1], row[2]))
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return "Inserted the contact successfully."
    except Exception as exc: 
        return "Something went wrong when inserting the contact:\n" + str(exc)

def insertManyRows(rows):    
    command = """
        CREATE OR REPLACE PROCEDURE insertManyContacts(firstnames VARCHAR[], lastnames VARCHAR[], phones VARCHAR[])
        LANGUAGE plpgsql
        AS $$
        DECLARE
            currentFN VARCHAR(255);
            currentLN VARCHAR(255);
            currentPhone VARCHAR(255);
        BEGIN
            FOR currentIndex IN 1..GREATEST(array_length(firstnames, 1), array_length(lastnames, 1), array_length(phones, 1)) LOOP
                currentFN := firstnames[currentIndex];
                currentLN := lastnames[currentIndex];
                currentPhone := phones[currentIndex];
                
                IF currentPhone IS NULL OR length(currentPhone) > 12 THEN
                    RAISE NOTICE 'ERROR: Invalid phone for % % - Phone: %', 
                        currentFN, currentLN, currentPhone;
                    CONTINUE;
                END IF;
                
                IF currentFN IS NULL OR currentFN = '' THEN
                    RAISE NOTICE 'ERROR: Empty firstname for % - Phone: %', 
                        currentLN, currentPhone;
                    CONTINUE;
                END IF;
                
                IF currentLN IS NULL OR currentLN = '' THEN
                    RAISE NOTICE 'ERROR: Empty lastname for % - Phone: %', 
                        currentFN, currentPhone;
                    CONTINUE;
                END IF;
                
                INSERT INTO users(firstname, lastname, phone) VALUES(currentFN, currentLN, currentPhone);
            END LOOP;
        END;
        $$;
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        resetSerial()
        
        firstnames = [row[0] for row in rows]
        lastnames = [row[1] for row in rows]
        phones = [row[2] for row in rows]
    
        cursor.execute(command)
        cursor.execute("CALL insertManyContacts(%s, %s, %s)", (firstnames, lastnames, phones))
        
        messages = ["\n"]
        
        if connection.notices:
            for notice in connection.notices:
                messages.append(notice)
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return f"Inserted contacts successfully. {"\n".join(messages)}"
    except Exception as exc: 
        return "Something went wrong when inserting multiple contacts:\n" + str(exc)

def updatePhone(id = 0, fname = "", lname = "", phone = "", newPhone = ""):
    if id == 0 and fname == "" and lname == "" and phone == "":
        return "No filters provided. Modification canceled."
    elif newPhone == "":
        return "New phone not provided. Modification canceled."
    else:
        command = """
            UPDATE users SET phone = %(newPhone)s
            WHERE (%(id)s = 0 OR userid = %(id)s)
            AND firstname ILIKE '%%' || %(fname)s || '%%'
            AND lastname ILIKE '%%' || %(lname)s || '%%'
            AND phone ILIKE '%%' || %(phone)s || '%%';
        """
        
        try:
            connection = connect()
            cursor = connection.cursor()
            
            cursor.execute(command, {
                "id" : id,
                "fname" : fname,
                "lname" : lname,
                "phone" : phone,
                "newPhone" : newPhone
            }) 
            
            connection.commit()    
            
            cursor.close()
            connection.close()
            
            return "Updated the phone successfully."
        except Exception as exc: 
            return "Something went wrong when updating the phone:\n" + str(exc)
        
def queryRows(fname = "", lname = "", desc = True):
    selectedRows = None
    
    command = "SELECT * FROM users"
    
    parameters = []
    filters = []
    
    if fname:
        filters.append("firstname ILIKE %s")
        parameters.append(fname)
    if lname:
        filters.append("lastname ILIKE %s")
        parameters.append(lname)
        
    if filters:
        command += " WHERE " + " AND ".join(filters)
        
    sort = "DESC" if desc else "ASC"
    command += f" ORDER BY userid {sort};"
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute(command, tuple(parameters))
        selectedRows = cursor.fetchall()
        
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return selectedRows
    except Exception as exc:
        return "Something went wrong when selecting contacts:\n" + str(exc)

def deleteRow(id = 0, fname = "", lname = "", phone = ""):
    if id == 0 and fname == "" and lname == "" and phone == "":
        return "No filters provided. Deletion canceled."
    else:
        command = """
            CREATE OR REPLACE PROCEDURE deleteContact(id INTEGER, fname VARCHAR, lname VARCHAR, phoneNum VARCHAR)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                DELETE FROM users
                WHERE (id = 0 OR userid = id)
                AND firstname ILIKE '%' || fname || '%'
                AND lastname ILIKE '%' || lname || '%'
                AND phone ILIKE '%' || phoneNum || '%';
            END;
            $$;
        """

        try:
            connection = connect()
            cursor = connection.cursor()

            cursor.execute(command)
            cursor.execute("CALL deleteContact(%s, %s, %s, %s)", (id, fname, lname, phone)) 
            
            connection.commit()    

            cursor.close()
            connection.close()

            return f"Deleted contact(s) successfully."
        except Exception as exc: 
            return "Something went wrong when deleting the contact:\n" + str(exc)
    
def searchPattern(pattern, offset = 0, limit = 10):
    command = """
        CREATE OR REPLACE FUNCTION getContactsByPattern(pattern TEXT, currentOffset INTEGER, currentLimit INTEGER)
        RETURNS SETOF users
        LANGUAGE plpgsql
        AS $$
        BEGIN
            RETURN QUERY SELECT * FROM users
            WHERE firstname ILIKE '%' || pattern || '%'  
            OR lastname ILIKE '%' || pattern || '%'
            OR phone ILIKE '%' || pattern || '%'
            ORDER BY userid
            LIMIT currentLimit OFFSET currentOffset;
        END;
        $$;
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute(command)
        cursor.execute("SELECT * FROM getContactsByPattern(%s, %s, %s)", (pattern, offset, limit)) 
        contactList = cursor.fetchall()
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return contactList
    except Exception as exc: 
        return "Something went wrong when searching the contact:\n" + str(exc)

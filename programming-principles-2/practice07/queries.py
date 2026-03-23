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

def insertRow(row):
    command = """
        INSERT INTO users(firstname, lastname, phone) VALUES(%s, %s, %s);
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        resetSerial()
        cursor.execute(command, row)
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return "Inserted the row successfully."
    except Exception as exc: 
        return "Something went wrong when inserting the row:" + str(exc)

def insertManyRows(rows):
    command = """
        INSERT INTO users(firstname, lastname, phone) VALUES(%s, %s, %s);
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        resetSerial()
        cursor.executemany(command, rows)
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return "Inserted rows successfully."
    except Exception as exc: 
        return "Something went wrong when inserting multiple rows:" + str(exc)

def updatePhone(rowId, newPhone):
    command = """
        UPDATE users SET phone = %s WHERE userid = %s;
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute(command, (newPhone, rowId))
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return "Updated the phone successfully."
    except Exception as exc: 
        return "Something went wrong when updating the phone:" + str(exc)
        
def queryRows(fname = "", lname = "", asc = True):
    selectedRows = None
    
    command = "SELECT * FROM users"
    
    parameters = []
    filters = []
    
    if fname:
        filters.append("firstname = %s")
        parameters.append(fname)
    if lname:
        filters.append("lastname = %s")
        parameters.append(lname)
        
    if filters:
        command += " WHERE " + " AND ".join(filters)
        
    sort = "ASC" if asc else "DESC"
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
        return "Something went wrong when selecting rows:" + str(exc)

def deleteRowByPhone(phone):
    command = """
        DELETE FROM users WHERE phone = %s;
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute(command, (phone,))   # Trailing comma for a single element tuple!
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return "Deleted the row successfully."
    except Exception as exc: 
        return "Something went wrong when deleting the row:" + str(exc)
    
    
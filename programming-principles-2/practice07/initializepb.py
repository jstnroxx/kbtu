from connect import connect

def initPhonebook():
    command = """
        CREATE TABLE IF NOT EXISTS users (
            userid SERIAL PRIMARY KEY,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            phone VARCHAR(12) NOT NULL
        );
    """
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute(command)
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return "Initialized phonebook successfully."
    except Exception as exc: 
        return "Something went wrong when initializing the phonebook:" + str(exc)
    
def initTestPhones(rowAmount = 3):
    command = """
        INSERT INTO users(firstname, lastname, phone) VALUES ('Firstname%s', 'Lastname%s', 'PhoneNo%s');
    """

    try:
        connection = connect()
        cursor = connection.cursor()
        
        cursor.execute("SELECT MAX(userid) FROM users;")
        lastid = cursor.fetchone()[0] or 0
        cursor.execute(f"ALTER SEQUENCE users_userid_seq RESTART WITH {lastid + 1};")
        
        for num in range(lastid + 1, (rowAmount + lastid) % 10000 + 1):
            cursor.execute(command, (num, num, num))
        
        connection.commit()    
        
        cursor.close()
        connection.close()
        
        return "Inserted phonebook test rows successfully."
    except Exception as exc: 
        return "Something went wrong when inserting phonebook test rows:" + str(exc)
    
if __name__ == "__main__":
    initPhonebook()
    initTestPhones()
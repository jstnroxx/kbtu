from pathlib import Path

from .connect import connect

sqlFolderPath = Path(__file__).parent.parent / "sql"

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
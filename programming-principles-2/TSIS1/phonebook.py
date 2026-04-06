import psycopg2
from connect import connect

# Utilities ################################
def readFromSQL(filename, tag = ""):
    try:
        with open(filename) as file:
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
        
# Database interaction ################################
def createSchema():
    try:
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(readFromSQL("schema.sql"))
            
    except psycopg2.Error as Err:
        print(Err)
        
    finally:
        if connection:
            connection.close()
        
# Debug
# if __name__ == "__main__":
#     createSchema()
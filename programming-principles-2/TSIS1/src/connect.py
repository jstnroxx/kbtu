import psycopg2

from .config import loadConfig

# Get database connection object
def connect():
    try:
        config = loadConfig()
        
        try:
            with psycopg2.connect(**config) as conn:
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    except:
        print("Failed to get database configurations.")
        
# Run connection process if the file is run as main
if __name__ == "__main__":
    connect()
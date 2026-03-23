import psycopg2
from config import loadConfig

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print("Connected to PostgreSQL server.")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
if __name__ == "__main__":
    config = loadConfig()
    connect(config)
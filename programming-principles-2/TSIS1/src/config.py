from pathlib import Path
from configparser import ConfigParser

fileDirectoryPath = Path(__file__).parent

# Create database configurations
def loadConfig(filename = "database.ini", section = "postgresql"):
    configFilePath = fileDirectoryPath / filename
    
    parser = ConfigParser()
    parser.read(configFilePath)
    
    config = {}
    
    if parser.has_section(section):
        params = parser.items(section)
        
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f"Section {0} not found in the {1} file".format(section, filename))
    
    return config

# Show database configurations if the file is run directly
if __name__ == "__main__":
    config = loadConfig()
    print(config)
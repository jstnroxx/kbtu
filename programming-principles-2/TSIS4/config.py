import os

from configparser import ConfigParser


def load_db_config(filename: str = "database.ini", section: str = "postgresql") -> dict:
    path = os.path.join(os.path.dirname(__file__), filename)
    parser = ConfigParser()
    
    if not parser.read(path):
        raise FileNotFoundError(f"Config file '{path}' not found.")
    if not parser.has_section(section):
        raise KeyError(f"Section '{section}' not found in '{path}'.")
    
    return dict(parser.items(section))
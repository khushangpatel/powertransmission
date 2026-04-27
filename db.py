import sqlite3

def get_connection():
    return sqlite3.connect("transmission_system.db", check_same_thread=False)
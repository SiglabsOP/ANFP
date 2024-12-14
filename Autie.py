import os                             
import time
import sqlite3
from datetime import datetime            # AUTIE v 31.074 (c) 2024 SIG LABS - Peter De Ceuster https://peterdeceuster.uk/index2.html

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS changes (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                content TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)

def log_changes(conn, content_before, content_after):
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        changes = set(content_after.splitlines()) - set(content_before.splitlines())

        if changes:
            changes_text = "\n".join(changes)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO changes (timestamp, content) VALUES (?, ?)', (timestamp, changes_text))
            conn.commit()
            # If writing to SQLite database succeeds, also append to FALLBACK.txt
            append_to_fallback(timestamp, changes_text)
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # If writing to SQLite database fails, fallback to appending to FALLBACK.txt
        append_to_fallback(timestamp, changes_text)

def append_to_fallback(timestamp, changes_text):
    try:
        with open('FALLBACK.txt', 'a', encoding='utf-8') as fallback_file:
            fallback_file.write(f"\nChanges detected at {timestamp}:\n{changes_text}\n")
    except Exception as e:
        print("Error appending to fallback file:", e)

def copy_changes(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT content FROM changes ORDER BY timestamp DESC LIMIT 1')
        result = cursor.fetchone()

        if result:
            with open('BINGLISTCHANGES.txt', 'a', encoding='utf-8') as changes_file:
                changes_file.write(f"\nChanges detected at {datetime.now()}:\n{result[0]}\n")
    except sqlite3.Error as e:
        print("SQLite error:", e)

def check_file_changes():
    original_file = 'BINGLIST.txt'
    db_file = 'changes.db'

    try:
        conn = sqlite3.connect(db_file)
        create_table(conn)

        with open(original_file, 'r', encoding='utf-8') as file:
            original_content = file.read()

        while True:
            time.sleep(10)

            with open(original_file, 'r', encoding='utf-8') as file:
                current_content = file.read()

            if current_content != original_content:
                log_changes(conn, original_content, current_content)
                copy_changes(conn)

                original_content = current_content
    except FileNotFoundError as e:
        print("File not found error:", e)
    except sqlite3.Error as e:
        print("SQLite error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    check_file_changes()

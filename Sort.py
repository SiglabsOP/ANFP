import sqlite3
from datetime import datetime, timedelta

def remove_old_entries():
    # Connect to the database
    conn = sqlite3.connect('changes.db')
    cursor = conn.cursor()

    # Retrieve entries from the changes table
    cursor.execute('SELECT timestamp, content FROM changes')
    entries = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Get the current system time
    current_time = datetime.now()

    # Open BINGLIST.txt and read the content
    with open('BINGLIST.txt', 'r', encoding='utf-8') as binglist_file:
        binglist_content = binglist_file.read()

    print(f"BINGLIST Content Before Removal:\n{binglist_content}")

    # Initialize a list to store removed entries
    removed_entries = []

    # Iterate over entries from the database
    for timestamp, entry in entries:
        entry_date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

        # Print information for debugging
        print(f"Entry Date: {entry_date}")
        print(f"Current Time: {current_time}")
        print(f"Time Difference: {current_time - entry_date}")
        print(f"Condition 1: {current_time - entry_date > timedelta(minutes=1)}")

        # Print the exact entry we are checking for
        print(f"Checking for entry:\n{entry}")

        # Check if there's a match in BINGLIST.txt and apply the one-minute condition or 24h
        if entry in binglist_content and (current_time - entry_date).total_seconds() > 24 * 60 * 60:
            print(f"Removing: {entry}")
            # Remove only the specific entry from BINGLIST.txt
            binglist_content = binglist_content.replace(entry, "").strip()

            # Print the content of binglist_content after removal
            print(f"BINGLIST Content After Removal:\n{binglist_content}")

            # Add the removed entry to the list
            removed_entries.append(f"{timestamp} - {entry}")

    # Write the updated content to BINGLIST.txt with UTF-8 encoding
    with open('BINGLIST.txt', 'w', encoding='utf-8') as binglist_file:
        binglist_file.write(binglist_content)

    # Write the removed entries to REMOVALS.txt
    with open('REMOVALS.txt', 'a') as removals_file:
        removals_file.write('\n'.join(removed_entries))

if __name__ == "__main__":
    remove_old_entries()

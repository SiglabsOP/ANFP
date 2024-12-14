import os

def remove_duplicate_lines(file_path):
    if not os.path.exists(file_path):
        print("File Not Found: The file does not exist.")
        return

    encodings = ['utf-8', 'latin-1', 'cp1252']  # Add more encodings if necessary
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                lines = file.readlines()
            break  # Break out of the loop if no decoding error occurs
        except UnicodeDecodeError:
            continue  # Try the next encoding if decoding error occurs

    unique_lines = set()
    lines_to_write = []
    removed_lines = []

    for line in lines:
        if line not in unique_lines:
            unique_lines.add(line)
            lines_to_write.append(line)
        else:
            removed_lines.append(line)

    with open(file_path, 'w', encoding=encoding) as file:
        file.writelines(lines_to_write)

    with open('dupesremoved.log', 'a') as log_file:
        if removed_lines:
            log_file.write(f"Duplicate lines removed from {file_path}:\n")
            for line in removed_lines:
                log_file.write(f"Removed: {line.strip()}\n")
        else:
            log_file.write(f"No duplicate lines found in {file_path}\n")

if __name__ == "__main__":
    file_name = "binglist.txt"
    remove_duplicate_lines(file_name)

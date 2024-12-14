import os

# Function to replace specific odd characters with '?' add  '–', also if needed
def replace_odd_characters(line):
    odd_characters = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', ' ']
    replaced_line = ""
    for char in line:
        if char in odd_characters:  # Replace specific odd characters with '?'
            replaced_line += '?'
        else:
            replaced_line += char
    return replaced_line

# Open the original text file with utf-8 encoding
with open("combined_report.txt", "r", encoding='utf-8') as original_file:
    # Read all lines from the original file
    lines = original_file.readlines()

# Create a new formatted text file
with open("combined_reportOK.txt", "w", encoding='utf-8') as formatted_file, open("formaterrors.txt", "w", encoding='utf-8') as error_file:
    # Iterate through lines starting from the second line (skip the first line which contains the headline)
    for line in lines[1:]:
        # Replace specific odd characters with '?'
        formatted_line = replace_odd_characters(line)
        
        # Split the line into headline and URL
        parts = formatted_line.strip().split("\t")

        # Check if the line has at least two elements (headline and URL)
        if len(parts) >= 2:
            # If both headline and URL are present, write the formatted line to the new file with hashtags added
            formatted_file.write(f"#autismsupport #autismnews {parts[0]}\t{parts[1]}\n")
        else:
            # If either headline or URL is missing, skip writing the line
            error_file.write(f"Error: Line does not have expected structure: {formatted_line}")

print("Formatting completed. Check 'combined_reportOK.txt' and 'formaterrors.txt'")

# Delete the original file
os.remove("combined_report.txt")

# Rename the formatted file to the binglist format
os.rename("combined_reportOK.txt", "binglist.txt")

print("Clean. Formatted file made ready as 'binglist.txt'")

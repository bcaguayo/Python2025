# tocomma.py
FILENAME = "clients.txt"

# filename = input("Enter the name of the .txt file: ")
out = ""

try:
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    out = "; ".join(lines)
except IOError as e:
    print(f"File '{FILENAME}' not found.")

# print(out)

OUTNAME = "prose.txt"

# Write to a new file
try:
    with open(OUTNAME, 'w', encoding='utf-8') as outfile:
        outfile.write(out)
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
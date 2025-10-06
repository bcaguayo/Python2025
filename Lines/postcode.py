# tocomma.py
FILENAME = "code.txt"
OUTNAME = "postcodes.txt"

# filename = input("Enter the name of the .txt file: ")

try:
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = [line.strip().rsplit(",", maxsplit=1)[1] + '\n' for line in file]
except IndexError as e:
    # Continue
    pass
except IOError as e:
    print(f"File '{FILENAME}' not found.")


# Write to a new file
try:
    with open(OUTNAME, 'w', encoding='utf-8') as outfile:
            outfile.writelines(lines)
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
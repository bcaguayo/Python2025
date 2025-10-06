# tocomma.py
FILENAME = "copypaste.txt"
OUTNAME = "addresses.txt"

# filename = input("Enter the name of the .txt file: ")

lines = []

try:
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = [line.strip().rsplit(",", maxsplit=1)[1].strip() + '\n' if line.strip() and "," in line else '\n' for line in file]
except IOError as e:
    print(f"File '{FILENAME}' not found.")


# Write to a new file
try:
    with open(OUTNAME, 'w', encoding='utf-8') as outfile:
        outfile.writelines(lines)
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")

# line.strip().split(" ", maxsplit=1)[1] + '\n' if " " in line else '\n' for line in file
# line.strip().rsplit(",", maxsplit=1)[1].strip() + '\n' if line.strip() and "," in line else '\n' for line in file
# line.strip().split(",", maxsplit=1)[1].rsplit(",", maxsplit=1)[0].strip()
# line.strip().rsplit(",", maxsplit=1)[1].strip()
# line.strip().split(",", maxsplit=1)[1].rsplit(",", maxsplit=1)[0].strip() 
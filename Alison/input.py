yipee = input("Please enter something: ")

print(f"You entered: {yipee}")

with open('op.txt', 'a+') as out:
    out.write(yipee)
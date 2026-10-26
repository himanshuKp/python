with open("olympics.txt", "r") as file:
    lines = file.readlines()
    chars = sum(len(line) for line in lines)

print("Total number of lines:", len(lines))
print("First line:", lines[0].strip())
print("Total number of characters:", chars)
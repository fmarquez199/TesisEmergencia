from sys import argv

with open(argv[1] + ".tbl", "r") as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    new_lines.append(line[:-2] + "\n")

with open(argv[1] + ".tbl", "w") as file:
    file.writelines(new_lines)
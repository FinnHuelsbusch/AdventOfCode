import re
import numpy as np

try: 
    with open("./Day3/input.txt") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    numbers = []
    total_sum = 0
    # get the index of the first digit of all numbers in a line 
    for line_index, line in enumerate(lines):
        p = re.compile(r"\d+")
        for m in p.finditer(line):
            numbers.append(((max(0, line_index-1), max(m.start()-1,0)), (line_index+2, m.end()+1), int(m.group())))
    # convert lines to a 2d np array
    lines = np.array([list(line.strip()) for line in lines])
    for entry in numbers:
        # select widow from top left to bottom right
        window = lines[entry[0][0]:entry[1][0], entry[0][1]:entry[1][1]].flatten()
        # check if any character in the window is different from a digit or a dot
        if re.search(r"[^\d\.]", "".join(window)) is not None:
            total_sum += entry[2]
            print(entry[2])
    print(total_sum)
        
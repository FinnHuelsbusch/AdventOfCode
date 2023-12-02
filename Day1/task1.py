import re

try:
    total_sum = 0
    # open file and read line by line
    with open("input.txt") as f:
        for line in f:
            # find all single digits in the line
            matches = re.findall(r"[1-9]", line)
            # combine first and last digit to a number and add it to the total sum
            total_sum += int(matches[0] + matches[-1])
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    print(total_sum)

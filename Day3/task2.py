import re
import numpy as np

try: 
    with open("./Day3/input.txt") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    gears = []
    total_sum = 0
    # get a 3x3 window around each gear
    for line_index, line in enumerate(lines):
        p = re.compile(r"\*")
        for m in p.finditer(line):
            gears.append(((max(0, line_index-1), max(m.start()-1,0)), (line_index+2, m.end()+1)))
    # convert lines to a 2d np array
    lines = np.array([list(line.strip()) for line in lines])
    for entry in gears:
        # select widow from top left to bottom right of the gear
        window = lines[entry[0][0]:entry[1][0], entry[0][1]:entry[1][1]]
        position_of_number = []
        # get the position of the numbers in the window
        for line_index, line in enumerate(window):
            p = re.compile(r"\d+")
            # check if any character in the line is a number
            for m in p.finditer("".join(line)):
                # get the original position of the number
                position_of_number.append((entry[0][0]+line_index, entry[0][1]+m.start()))
        # check if there are two numbers in the window
        if 2 == len(position_of_number):
            # enlarge number window until it contains all digits of the number
            while re.search(r"\d", lines[position_of_number[0]]) is not None:
                position_of_number[0] = (position_of_number[0][0], position_of_number[0][1]-1)
                if position_of_number[0][1] == 0:
                    break
            while re.search(r"\d", lines[position_of_number[1]]) is not None:
                position_of_number[1] = (position_of_number[1][0], position_of_number[1][1]-1)
                if position_of_number[1][1] == 0:
                    break
            # get the number
            helper = "".join(lines[position_of_number[0][0], position_of_number[0][1]:])
            number1 = re.findall(r"\d+", helper)[0]
            helper = "".join(lines[position_of_number[1][0], position_of_number[1][1]:]) 
            number2 = re.findall(r"\d+", helper)[0]
            # multiply numbers
            total_sum += int(number1) * int(number2)
    print(total_sum)

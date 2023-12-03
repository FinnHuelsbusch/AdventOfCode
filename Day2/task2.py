import re 

try: 
    with open("./input.txt") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    total_sum = 0
    for index, line in enumerate(lines):
        blue_matches = re.findall(r"\d+(?= blue)", line)
        blue_matches = list(map(int, blue_matches))
        green_matches = re.findall(r"\d+(?= green)", line)
        green_matches = list(map(int, green_matches))
        red_matches = re.findall(r"\d+(?= red)", line)
        red_matches = list(map(int, red_matches))
        total_sum +=  max(blue_matches) * max(green_matches) * max(red_matches)
    print(total_sum)
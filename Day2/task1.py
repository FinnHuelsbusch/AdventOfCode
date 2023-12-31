import re 

MAXIMUM_NUMBER_OF_CUBES = {
    "red": 12, 
    "green": 13,
    "blue" : 14
}

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
        total_sum += (index+1) * (MAXIMUM_NUMBER_OF_CUBES["blue"] >= max(blue_matches)) * (MAXIMUM_NUMBER_OF_CUBES["green"] >= max(green_matches)) * (MAXIMUM_NUMBER_OF_CUBES["red"] >= max(red_matches))
    print(total_sum)
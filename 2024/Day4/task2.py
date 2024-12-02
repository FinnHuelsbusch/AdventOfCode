import re
from collections import Counter
try: 
    with open("./Day4/input.txt") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    total_number_of_scratch_cards = 0
    repeat_dict = {}
    for line_index, line in enumerate(lines):
        winning_numbers = re.findall(r"[\d,\s]* (?=\|)", line)[0]
        winning_numbers = [int(elem) for elem in winning_numbers.strip().replace("  ", " ").split(" ")]
        numbers_you_have = re.findall(r"(?<=\|) [\d,\s]*", line)[0]
        numbers_you_have = [int(elem) for elem in numbers_you_have.strip().replace("  ", " ").split(" ")]
        counter_winning_numbers = Counter(winning_numbers)
        counter_numbers_you_have = Counter(numbers_you_have)

        # Find the common elements and their counts
        common_elements_with_counts = counter_winning_numbers & counter_numbers_you_have
        total_number_of_common_elements = sum(common_elements_with_counts.values())
        for iteration in range(repeat_dict.get(line_index, 0) + 1):
            total_number_of_scratch_cards += 1
            for i in range(total_number_of_common_elements):
                repeat_dict[line_index+i+1] = repeat_dict.get(line_index+i+1, 0) + 1
            
                
                
    print(total_number_of_scratch_cards)
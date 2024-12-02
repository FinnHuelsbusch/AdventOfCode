import re
from collections import Counter
try: 
    with open("./Day4/input.txt") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    total_sum = 0
    for line in lines:
        winning_numbers = re.findall(r"[\d,\s]* (?=\|)", line)[0]
        winning_numbers = [int(elem) for elem in winning_numbers.strip().replace("  ", " ").split(" ")]
        numbers_you_have = re.findall(r"(?<=\|) [\d,\s]*", line)[0]
        numbers_you_have = [int(elem) for elem in numbers_you_have.strip().replace("  ", " ").split(" ")]
        counter_winning_numbers = Counter(winning_numbers)
        counter_numbers_you_have = Counter(numbers_you_have)

        # Find the common elements and their counts
        common_elements_with_counts = counter_winning_numbers & counter_numbers_you_have
        total_number_of_common_elements = sum(common_elements_with_counts.values())
        if total_number_of_common_elements > 0:
            
            total_sum += 1*2**(total_number_of_common_elements-1)
    print(total_sum)
import re


WORD_TO_NUMBER_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def word_to_number(word: str):
    """Converts the word representation of a number to the number itself as a string.

    Args:
        word (str): The word representation of a number

    Returns:
        str: The number as a string
    """
    value = None
    if word.isnumeric():
        value = word
    else:
        value = WORD_TO_NUMBER_DICT[word]
    return value


try:
    total_sum = 0
    # open file and read line by line
    with open("input.txt") as f:
        for line in f:
            # find all single digits in the line or words representing numbers including overlapping matches
            matches = re.findall(
                r"(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", line
            )
            # combine first and last digit to a number and add it to the total sum
            total_sum += int(word_to_number(matches[0]) + word_to_number(matches[-1]))
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    print(total_sum)

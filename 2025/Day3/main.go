package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func task1() {
	// read the input file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// concat the input file into a string
	var input string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input += scanner.Text() + "\n"
	}

	// apply regex to extract the numbers
	var result = 0
	re := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	for _, match := range re.FindAllString(input, -1) {
		numbers := re.FindStringSubmatch(match)

		// convert the numbers to integers
		num1, _ := strconv.Atoi(numbers[1])
		num2, _ := strconv.Atoi(numbers[2])
		result += num1 * num2
	}
	fmt.Printf("Result for task1: %d\n", result)

	// split the input after every match of the regex but keep the matches at the end of the strings
	inputs := re.Split(input, -1)
	result = 0
	var i = 0

	index_of_last_do_not := -1
	index_of_last_do := -1
	// check if "do_not" is present in the input
	for _, match := range re.FindAllString(input, -1) {
		fmt.Printf("inputs[i]: %s\n", inputs[i])
		if strings.Contains(inputs[i], "don't()") {
			fmt.Printf("inputs[i]: %s\n", inputs[i])
			index_of_last_do_not = i
		}
		if strings.Contains(inputs[i], "do()") {
			index_of_last_do = i
		}
		if index_of_last_do_not != -1 && index_of_last_do_not == index_of_last_do && strings.LastIndex(inputs[i], "don't()") > strings.LastIndex(inputs[i], "do()") {
			i++
			continue
		}

		if index_of_last_do_not != -1 && index_of_last_do_not > index_of_last_do {
			i++
			continue
		}

		numbers := re.FindStringSubmatch(match)

		// convert the numbers to integers
		num1, _ := strconv.Atoi(numbers[1])
		num2, _ := strconv.Atoi(numbers[2])
		fmt.Printf("num1: %d * num2: %d\n", num1, num2)
		result += num1 * num2

		i++
	}
	fmt.Printf("Result for task2: %d\n", result)

}

func main() {
	task1()
}

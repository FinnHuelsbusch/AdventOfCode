package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func task1() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var safeReports = 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		numbers_string := strings.Split(line, " ")
		var numbers = make([]int, len(numbers_string))
		for i := 0; i < len(numbers_string); i++ {
			numbers[i], _ = strconv.Atoi(numbers_string[i])
		}
		var valid = true
		var increasing bool
		if numbers[0] < numbers[1] {
			increasing = true
		} else {
			increasing = false
		}
		for i := 1; i < len(numbers); i++ {
			if increasing && (numbers[i] <= numbers[i-1] || numbers[i]-numbers[i-1] > 3) {
				valid = false
				break
			} else if !increasing && (numbers[i-1]-numbers[i] < 1 || numbers[i-1]-numbers[i] > 3) {
				valid = false
				break
			}
		}
		if valid {
			safeReports++
		}
	}
	fmt.Println(safeReports)

}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func task2() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var safeReports = 0
	scanner := bufio.NewScanner(file)
	var index = 0
	for scanner.Scan() {
		line := scanner.Text()
		numbers_string := strings.Split(line, " ")
		var numbers = make([]int, len(numbers_string))
		for i := 0; i < len(numbers_string); i++ {
			numbers[i], _ = strconv.Atoi(numbers_string[i])
		}

		if isValid(numbers, true) {
			safeReports++
		}
		index++
	}
	fmt.Println(safeReports)
}
func RemoveIndex(s []int, index int) []int {
	var s_new = make([]int, len(s))
	copy(s_new, s)
	return append(s_new[:index], s_new[index+1:]...)
}

func isValid(numbers []int, firstTry bool) bool {
	var increasing bool
	if numbers[0] < numbers[1] {
		increasing = true
	} else {
		increasing = false
	}
	for i := 1; i < len(numbers); i++ {
		if increasing && (numbers[i]-numbers[i-1] < 1 || numbers[i]-numbers[i-1] > 3) {
			if firstTry {
				numbers_without_i := RemoveIndex(numbers, i)
				numbers_without_i_1 := RemoveIndex(numbers, i-1)
				return isValid(numbers_without_i, false) || isValid(numbers_without_i_1, false)
			} else {
				return false
			}
		} else if !increasing && (numbers[i-1]-numbers[i] < 1 || numbers[i-1]-numbers[i] > 3) {
			if firstTry {
				numbers_without_i := RemoveIndex(numbers, i)
				numbers_without_i_1 := RemoveIndex(numbers, i-1)
				return isValid(numbers_without_i, false) || isValid(numbers_without_i_1, false)
			} else {
				return false
			}
		}
	}
	return true
}

func main() {
	task2()
}

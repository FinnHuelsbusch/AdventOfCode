package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

	var list1, list2 []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Split(line, "   ")
		if len(numbers) == 2 {
			num1, err1 := strconv.Atoi(numbers[0])
			num2, err2 := strconv.Atoi(numbers[1])
			if err1 == nil && err2 == nil {
				list1 = append(list1, num1)
				list2 = append(list2, num2)
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
	sort.Ints(list1)
	sort.Ints(list2)
	var result int
	i, j := 0, 0

	for i < len(list1) && j < len(list2) {
		if list1[i] == list2[j] {
			result += list1[i]
			i++
			j++
		} else if list1[i] < list2[j] {
			i++
		} else {
			j++
		}
	}

	fmt.Printf("Result: %d\n", result)
}

func main() {
	task2()
}

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
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

	var list1, list2 []float64

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Split(line, "   ")
		if len(numbers) == 2 {
			num1, err1 := strconv.ParseFloat(numbers[0], 64)
			num2, err2 := strconv.ParseFloat(numbers[1], 64)
			if err1 == nil && err2 == nil {
				list1 = append(list1, num1)
				list2 = append(list2, num2)
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
	sort.Float64s(list1)
	sort.Float64s(list2)
	var difference float64 = 0.0

	// iterate over lists
	for i := 0; i < len(list1); i++ {
		difference += math.Abs(list1[i] - list2[i])
	}
	fmt.Printf("Difference: %.10f\n", difference)

}

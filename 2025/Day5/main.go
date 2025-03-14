package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func task1() {
	// read the input file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// read the input file into a slice of strings
	var rules []string
	var pages []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}
	fmt.Printf("input:\n")
	for i := 0; i < len(input); i++ {
		fmt.Printf("%s\n", input[i])
	}


}

func main() {
	task1()
}

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
	var input []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}
	fmt.Printf("input:\n")
	for i := 0; i < len(input); i++ {
		fmt.Printf("%s\n", input[i])
	}

	// apply regex to extract the numbers
	re := regexp.MustCompile(`SAMX`)
	re2 := regexp.MustCompile(`XMAS`)
	// count the number of matches
	result := 0
	for i := 0; i < len(input); i++ {
		result += len(re.FindAllString(input[i], -1))
		result += len(re2.FindAllString(input[i], -1))
	}

	fmt.Printf("result after checking horizontal: %d\n", result)

	for i := 0; i < len(input); i++ {
		for j := 0; j < len(input[i]); j++ {
			if i != 0 && j != 0 {
				break
			}
			var diagonalstring string
			diagonalstring += string(input[i][j])
			l := j
			for k := i + 1; k < len(input); k++ {
				if l+1 < len(input[k]) {
					l++
					diagonalstring += string(input[k][l])
				} else {
					break
				}
			}
			result += len(re2.FindAllString(diagonalstring, -1))
			result += len(re.FindAllString(diagonalstring, -1))
		}
	}

	fmt.Printf("result after checking diagonal: %d\n", result)

	for i := len(input) - 1; i >= 0; i-- {
		for j := 0; j < len(input[i]); j++ {
			if i != len(input)-1 && j != 0 {
				break
			}
			var diagonalstring string
			diagonalstring += string(input[i][j])
			l := j
			for k := i - 1; k >= 0; k-- {
				if l+1 < len(input[k]) {
					l++
					diagonalstring += string(input[k][l])
				} else {
					break
				}
			}
			result += len(re.FindAllString(diagonalstring, -1))
			result += len(re2.FindAllString(diagonalstring, -1))
		}
	}

	for column := 0; column < len(input[0]); column++ {
		columnstring := ""
		for row := 0; row < len(input); row++ {
			columnstring += string(input[row][column])
		}
		result += len(re.FindAllString(columnstring, -1))
		result += len(re2.FindAllString(columnstring, -1))
	}

	fmt.Printf("result 1: %d\n", result)

	result = 0
	for i := 0; i <= len(input)-3; i++ {
		for j := 0; j <= len(input[i])-3; j++ {
			var diagonalstring1 string
			var diagonalstring2 string
			diagonalstring1 += string(input[i][j])
			diagonalstring2 += string(input[i][j+2])
			for k := 1; k < 3; k++ {
				diagonalstring1 += string(input[i+k][j+k])
				diagonalstring2 += string(input[i+k][j+2-k])
			}
			fmt.Print(diagonalstring1)
			fmt.Print(" ")
			fmt.Println(diagonalstring2)
			if len(diagonalstring1) != 3 {
				fmt.Printf("diagonalstring1: %s\n", diagonalstring1)
			}
			if len(diagonalstring2) != 3 {
				fmt.Printf("diagonalstring2: %s\n", diagonalstring2)
			}
			if (diagonalstring1 == "MAS" || diagonalstring1 == "SAM") && (diagonalstring2 == "MAS" || diagonalstring2 == "SAM") {
				result++
			}
		}
	}
	fmt.Printf("result 2: %d\n", result)

}

func main() {
	task1()
}

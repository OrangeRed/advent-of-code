//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"unicode"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var total int

	re := regexp.MustCompile("\\d+")

	lines := processStdIn()
	for row, line := range lines {
		for _, match := range re.FindAllStringIndex(line, -1) {
			//   -1012
			// -1 .*..
			//  0 .35.
			// +1 ....
			top := max(0, row-1)
			left := max(0, match[0]-1)
			bottom := min(len(lines)-1, row+1)
			right := min(len(line)-1, match[1])

			for _, schematic := range lines[top : bottom+1] {
				for _, char := range schematic[left : right+1] {
					if !(unicode.IsDigit(char) || string(char) == ".") {
						num, _ := strconv.Atoi(line[match[0]:match[1]])
						total += num
					}
				}
			}
		}
	}

	return total
}

func processStdIn() []string {
	var lines []string
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

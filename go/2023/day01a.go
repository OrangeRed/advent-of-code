//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var total int

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		line := scanner.Text()

		var numbers []int
		for i := 0; i < len(line); i++ {
			if unicode.IsDigit(rune(line[i])) {
				num, _ := strconv.Atoi(string(line[i]))

				numbers = append(numbers, num)
			}
		}

		total += numbers[0]*10 + numbers[len(numbers)-1]
	}

	return total
}

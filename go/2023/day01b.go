//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	fmt.Println(solve())
}

const words string = "one two three four five six seven eight nine"

func solve() int {
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))

	var total int
	for scanner.Scan() {
		line := scanner.Text()

		var numbers []int
		for i := 0; i < len(line); i++ {
			if unicode.IsDigit(rune(line[i])) {
				num, _ := strconv.Atoi(string(line[i]))
				numbers = append(numbers, num)
			} else {
				for j, word := range strings.Split(words, " ") {
					if strings.HasPrefix(line[i:], word) {
						numbers = append(numbers, j+1)
						break
					}
				}
			}
		}

		total += numbers[0]*10 + numbers[len(numbers)-1]
	}

	return total
}

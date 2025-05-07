//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	similarity := make(map[int]int)
	var left_numbers []int

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		numbers := strings.Fields(scanner.Text())

		left, err := strconv.Atoi(numbers[0])
		if err != nil {
			fmt.Println(err)
		}

		left_numbers = append(left_numbers, left)

		right, err := strconv.Atoi(numbers[1])
		if err != nil {
			fmt.Println(err)
		}

		if _, ok := similarity[right]; !ok {
			similarity[right] = 1
		} else {
			similarity[right]++
		}
	}

	total := 0
	for _, v := range left_numbers {
		if _, ok := similarity[v]; ok {
			total += v * similarity[v]
		}
	}

	return total
}

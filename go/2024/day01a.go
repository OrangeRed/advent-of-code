//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var left_numbers []int
	var right_numbers []int

	scanner := bufio.NewScanner(bufio.NewReader((os.Stdin)))
	for scanner.Scan() {
		numbers := strings.Fields(scanner.Text())
		left, err := strconv.Atoi(numbers[0])
		if err != nil {
			fmt.Println(err)
		}

		right, err := strconv.Atoi(numbers[1])
		if err != nil {
			fmt.Println(err)
		}

		left_numbers = append(left_numbers, left)
		right_numbers = append(right_numbers, right)
	}

	slices.Sort(left_numbers)
	slices.Sort(right_numbers)

	total := 0
	for i := range left_numbers {
		if left_numbers[i] > right_numbers[i] {
			total += left_numbers[i] - right_numbers[i]
		} else {
			total += right_numbers[i] - left_numbers[i]
		}
	}

	return total
}

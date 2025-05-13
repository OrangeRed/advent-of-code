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
	total := 0

	rules := make(map[int][]int)

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		line := scanner.Text()

		// Parse rules
		if strings.Contains(line, "|") {
			var before int
			var after int

			_, err := fmt.Sscanf(line, "%d|%d", &before, &after)
			if err != nil {
				fmt.Println(err)
			}

			rules[before] = append(rules[before], after)
		}

		// Parse print order
		if strings.Contains(line, ",") {
			correct := true

			var print_order []int
			for _, str := range strings.Split(line, ",") {
				current, err := strconv.Atoi(str)
				if err != nil {
					fmt.Println(err)
				}

				for _, ordered := range print_order {
					if slices.Contains(rules[current], ordered) {
						correct = false
						break
					}
				}

				print_order = append(print_order, current)
			}

			if correct {
				total += print_order[(len(print_order)-1)/2]
			}
		}
	}

	return total
}

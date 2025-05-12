//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"math"
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

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		levels_str := strings.Fields(scanner.Text())

		levels := make([]int, len(levels_str))
		for i, level := range levels_str {
			levels[i], _ = strconv.Atoi(level)
		}

		for i := range levels {
			if isSafe(slices.Concat(levels[:i], levels[i+1:])) {
				total += 1
				break
			}
		}
	}

	return total
}

func isSafe(levels []int) bool {
	asc, desc := true, true

	for i := 1; i < len(levels); i++ {
		if levels[i] > levels[i-1] {
			asc = false
		}

		if levels[i] < levels[i-1] {
			desc = false
		}

		diff := math.Abs(float64(levels[i] - levels[i-1]))
		if !(3 >= diff && diff >= 1) {
			return false
		}
	}

	if !(asc || desc) {
		return false
	}

	return true
}

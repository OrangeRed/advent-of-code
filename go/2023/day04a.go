//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var total int

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		// Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
		_cards, numbers, _ := strings.Cut(scanner.Text(), " | ")
		_, _winningCards, _ := strings.Cut(_cards, ": ")

		winningCards := make(map[string]bool)
		for _, card := range strings.Split(_winningCards, " ") {
			if _, exists := winningCards[card]; card != "" && !exists {
				winningCards[card] = true
			}
		}

		matches := 0
		for _, number := range strings.Split(numbers, " ") {
			if _, exists := winningCards[number]; number != "" && exists {
				matches += 1
			}
		}

		if matches > 0 {
			total += int(math.Pow(2, float64(matches-1)))
		}
	}

	return total
}

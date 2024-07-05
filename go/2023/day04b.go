//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var total int

	lines, scratchCards := processStdIn()
	for cardIdx, line := range lines {
		// Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
		_cards, numbers, _ := strings.Cut(line, " | ")
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

		scratchCards[cardIdx] += 1 // Default []int starts with zeros so +1 for the starting card.
		for match := 0; match < matches; match++ {
			if len(scratchCards) >= (cardIdx + 1 + match) {
				scratchCards[cardIdx+1+match] += scratchCards[cardIdx]
			}
		}
	}

	for _, number := range scratchCards {
		total += number
	}

	return total
}

func processStdIn() ([]string, []int) {
	var lines []string

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, make([]int, len(lines))
}

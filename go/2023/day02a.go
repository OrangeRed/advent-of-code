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
	var total int

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for scanner.Scan() {
		// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
		_gameId, games, _ := strings.Cut(scanner.Text(), ": ")
		gameId, _ := strconv.Atoi(strings.Replace(_gameId, "Game ", "", 1))

		if validate(games) {
			total += gameId
		}
	}

	return total
}

// games = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
func validate(games string) bool {
	validCubes := map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}

	for _, game := range strings.Split(games, "; ") {
		for _, cubes := range strings.Split(game, ", ") {
			_amount, color, _ := strings.Cut(cubes, " ")
			amount, _ := strconv.Atoi(_amount)

			if amount > validCubes[color] {
				return false
			}
		}
	}

	return true
}

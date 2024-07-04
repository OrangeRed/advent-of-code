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
		_, games, _ := strings.Cut(scanner.Text(), ": ")

		prod := 1
		for _, cubes := range getMinCubes(games) {
			prod *= cubes
		}

		total += prod
	}

	return total
}

// games = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
func getMinCubes(games string) map[string]int {
	minCubes := map[string]int{
		"red":   0,
		"green": 0,
		"blue":  0,
	}

	for _, game := range strings.Split(games, "; ") {
		for _, cubes := range strings.Split(game, ", ") {
			_amount, color, _ := strings.Cut(cubes, " ")
			amount, _ := strconv.Atoi(_amount)

			if amount > minCubes[color] {
				minCubes[color] = amount
			}
		}
	}

	return minCubes
}

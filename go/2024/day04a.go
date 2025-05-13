//go:build ignore

package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	fmt.Println(solve())
}

type Direction struct {
	dx int
	dy int
}

func solve() int {
	total := 0

	bytes, err := io.ReadAll(os.Stdin)
	if err != nil {
		fmt.Println(err)
	}

	grid := strings.Split(string(bytes), "\n")
	for y, line := range grid {
		for x, char := range line {
			if string(char) != "X" {
				continue
			}

			directions := []Direction{
				{dx: 0, dy: 1},
				{dx: 1, dy: 1},
			}

			for i := 0; i < 4; i++ {
				for idx, direction := range directions {
					// 90deg: (x, y) -> (-y, x)
					directions[idx] = Direction{
						dx: -direction.dy,
						dy: direction.dx,
					}

					if direction.dx == 1 && x >= len(line)-3 {
						continue
					}

					if direction.dx == -1 && x < 3 {
						continue
					}

					if direction.dy == 1 && y >= len(grid)-3 {
						continue
					}

					if direction.dy == -1 && y < 3 {
						continue
					}

					if isXMAS(&grid, x, y, direction) {
						total += 1
					}
				}
			}
		}
	}

	return total
}

func isXMAS(grid *[]string, x int, y int, dir Direction) bool {
	var word string

	for i := 0; i < len("XMAS"); i++ {
		word += string((*grid)[y+i*dir.dy][x+i*dir.dx])
	}

	return word == "XMAS"
}

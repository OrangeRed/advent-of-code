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
			if string(char) != "A" {
				continue
			}

			if !(len(grid)-1 > y && y >= 1 && len(line)-1 > x && x >= 1) {
				continue
			}

			direction := Direction{dx: 1, dy: 1}
			for i := 0; i < 4; i++ {
				// 90deg: (x, y) -> (-y, x)
				direction = Direction{
					dx: -direction.dy,
					dy: direction.dx,
				}

				if isXMAS(&grid, x, y, direction) {
					total += 1
				}
			}
		}
	}

	return total
}

func isXMAS(grid *[]string, x int, y int, dir Direction) bool {
	first := string([]byte{
		(*grid)[y+dir.dy][x+dir.dx],
		(*grid)[y][x],
		(*grid)[y-dir.dy][x-dir.dx]},
	)

	// 90deg: (x, y) -> (-y, x)
	rotated := Direction{dx: -dir.dy, dy: dir.dx}

	second := string([]byte{
		(*grid)[y+rotated.dy][x+rotated.dx],
		(*grid)[y][x],
		(*grid)[y-rotated.dy][x-rotated.dx]},
	)

	return first == "MAS" && second == "MAS"
}

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

type Coord struct {
	x int
	y int
}

func solve() int {
	var grid []string
	var guard Coord

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for i := 0; scanner.Scan(); i++ {
		line := scanner.Text()

		if strings.Contains(line, "^") {
			guard = Coord{x: strings.Index(line, "^"), y: i}
		}

		grid = append(grid, line)
	}

	return len(*walk(&grid, guard))
}

func walk(grid *[]string, guard Coord) *map[Coord]struct{} {
	dir := Coord{x: 0, y: -1}
	coordSet := map[Coord]struct{}{guard: {}}

	for true {
		next := Coord{x: guard.x + dir.x, y: guard.y + dir.y}

		if !(len((*grid)[0]) > next.x && next.x >= 0) {
			break
		}

		if !(len(*grid) > next.y && next.y >= 0) {
			break
		}

		if string((*grid)[next.y][next.x]) == "#" {
			// 90deg cw: (x, y) -> (-y, x)
			dir = Coord{x: -dir.y, y: dir.x}
			continue
		}

		guard = next
		if _, exists := coordSet[guard]; !exists {
			coordSet[guard] = struct{}{}
		}
	}

	return &coordSet
}

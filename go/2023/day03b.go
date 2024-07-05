//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	var total int

	re := regexp.MustCompile("\\d+")

	lines, gears := processStdIn()
	for row, line := range lines {
		for _, match := range re.FindAllStringIndex(line, -1) {
			//   -1012
			// -1 .*..
			//  0 .35.
			// +1 ....
			top := max(0, row-1)
			left := max(0, match[0]-1)
			bottom := min(len(lines)-1, row+1)
			right := min(len(line)-1, match[1])

			for _, gear := range gears {
				if gear.x >= left && gear.x <= right && gear.y >= top && gear.y <= bottom {
					num, _ := strconv.Atoi(line[match[0]:match[1]])
					if gear.value1 == 0 {
						gear.value1 = num
					} else {
						gear.value2 = num
					}
					break
				}
			}
		}
	}

	for _, gear := range gears {
		total += gear.value1 * gear.value2
	}

	return total
}

type GearCoords struct {
	x      int
	y      int
	value1 int
	value2 int
}

func processStdIn() ([]string, []*GearCoords) {
	var lines []string
	var gears []*GearCoords

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	for y := 0; scanner.Scan(); y++ {
		lines = append(lines, scanner.Text())
		for x, char := range scanner.Text() {
			if string(char) == "*" {
				gears = append(gears, &GearCoords{
					x:      x,
					y:      y,
					value1: 0,
					value2: 0,
				})
			}
		}
	}

	return lines, gears
}

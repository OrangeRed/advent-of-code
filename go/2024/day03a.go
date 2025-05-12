//go:build ignore

package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	total := 0

	bytes, err := io.ReadAll(os.Stdin)

	if err != nil {
		fmt.Print(err)
	}

	r, _ := regexp.Compile(`mul\(\d+,\d+\)`)

	for _, match := range r.FindAllString(string(bytes), -1) {
		var left int
		var right int

		if _, err := fmt.Sscanf(match, "mul(%d,%d)", &left, &right); err != nil {
			fmt.Println(err)
		}

		total += (left * right)
	}

	return total
}

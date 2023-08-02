package solutions

import (
	"os"
)

func Day01() string {
	input, err := os.ReadFile("../inputs/day01.txt")
	check(err)
	return string(input)

}

package solutions

import (
	"os"
)

func Day0X() string {
	input, err := os.ReadFile("../inputs/day0X.txt")
	check(err)
	return string(input)

}

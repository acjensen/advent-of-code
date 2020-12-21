// THE GO SOLUTION IS A WORK In PROGRESS

package main

import (
	"io/ioutil"
	"fmt"
	// "os"
	"path/filepath"
	"regexp"
)


func load_input(filename string) string {
	s, _ := ioutil.ReadFile(filename)
	return string(s)
}

type seat struct {
    id  int
	row int
	col int
	raw string
}

func newSeat(raw string) *seat {
	s := seat{raw: raw}
	for i, c := range s {
		if c == 'F' {
			
		}
	}

}

func main() {
	// pwd, _ := os.Getwd()
	filename := filepath.Join("day5","input.txt")
	s := load_input(filename)
	rows := regexp.MustCompile("\n").Split(s, -1)
	width := len(rows[0])
	height := len(rows)
	fmt.Println(height)
	fmt.Println(width)
	fmt.Println(rows)
	for i := 0; i < len(rows[0])
}

// this is a work in progress

package main

import (
	"fmt"
	"io/ioutil"
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

type seatmap struct {
	seat seat
}

// func newSeat(raw string) *seat {
// 	s := seat{raw: raw}
// 	for i, c := range s {
// 		if c == 'F' {

// 		}
// 	}

// }

/*

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

*/

func main() {
	// pwd, _ := os.Getwd()
	filename := filepath.Join("day11", "input.txt")
	s := load_input(filename)
	rows := regexp.MustCompile("\n").Split(s, -1)
	width := len(rows[0])
	height := len(rows)
	fmt.Println(height)
	fmt.Println(width)
	for i := 0; i < width; i++ {
		for j := 0; j < height; j++ {
			fmt.Println(i, j)
		}
	}
	var m map[string]map[int]float64
	m = make(map[string]map[int]float64)
	fmt.Println(m)
	myseat := seat{
		id:  1,
		row: 2,
		col: 3,
		raw: "L",
	}
	fmt.Println(myseat)
}

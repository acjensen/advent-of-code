// Some ideas...
// Thought: everything is a map... we're just mapping state to function back and forth...
//   the question is, when to use objects vs map keys
//   enums, if-thens, etc. eventually are just maps to other functions.
// Thought: Can I define this algebraically?
// Thought: Can I make the 'sim_func' a Go interface?

package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"regexp"
)

func main() {

	// Define constants.
	adjacent_seats := adjacent_seats()

	// Load seatmap into memory.
	pwd, _ := os.Getwd()
	s := load_text(filepath.Join(pwd, "input.txt"))
	my_seatmap := load_seatmaps(s)

	// Run part 1 and part 2 simulations.
	part_1 := sim_func_args{adjacent_seats, 4, false}
	part_2 := sim_func_args{adjacent_seats, 5, true}
	run_sim(my_seatmap, 100, adjacent_seats, part_1)
	run_sim(my_seatmap, 100, adjacent_seats, part_2)
}

type seatmap struct {
	seatmapstring [][]byte
	width         int
	height        int
}

type Seat struct {
	h, w int
}

// Load text from a file as one big string.
func load_text(filename string) string {
	s, _ := ioutil.ReadFile(filename)
	return string(s)
}

// Parse a string of seatmaps.
func load_seatmaps(s string) seatmap {
	rows := regexp.MustCompile("\n").Split(s, -1)
	width := len(rows[0])
	height := len(rows)
	rows_asbyte := make([][]byte, height)
	for r := range rows_asbyte {
		rows_asbyte[r] = []byte(rows[r])
	}
	smap := seatmap{rows_asbyte, width, height}
	return smap
}

// Define coordinates relative to the current seat to seats that are considered 'adjacent'.
func adjacent_seats() []Seat {
	return []Seat{{-1, 0}, {-1, 1}, {-1, -1}, {0, 1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}}
}

// Check if two seatmaps are equal.
func seatmap_equal(a *seatmap, b *seatmap) bool {
	for h := range a.seatmapstring {
		if string(a.seatmapstring[h]) != string(b.seatmapstring[h]) {
			return false
		}
	}
	return true
}

// Make an empty seatmap.
func make_seatmap(height int, width int) *seatmap {
	var smap_new seatmap
	rows_asbyte := make([][]byte, height)
	for r := range rows_asbyte {
		rows_asbyte[r] = make([]byte, width)
	}
	smap_new.seatmapstring = rows_asbyte
	smap_new.height = height
	smap_new.width = width
	return &smap_new
}

// Print the seatmap to the terminal.
func print_seatmap(smap seatmap) {
	for h := range smap.seatmapstring {
		fmt.Println(string(smap.seatmapstring[h]))
	}
}

func next_seat(this_seat byte, num_adj_occupied int, num_adj_occupied_tolerance int) byte {
	if this_seat == 'L' && num_adj_occupied == 0 {
		// If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
		return '#'
	} else if this_seat == '#' && num_adj_occupied >= num_adj_occupied_tolerance {
		// If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
		return 'L'
	} else if this_seat == '.' {
		// Floor (.) never changes; seats don't move, and nobody sits on the floor.
		return '.'
	} else {
		// Otherwise, the seat's state does not change.
		return this_seat
	}
}

type sim_func_args struct {
	adjacent_seats             []Seat
	num_adj_occupied_tolerance int
	queen_vision               bool
}

type sim_func interface {
	get_next_state(smap *seatmap) seatmap
}

func (a sim_func_args) get_next_state(smap *seatmap) seatmap {

	/*
		If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
		If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
		Otherwise, the seat's state does not change.
		Floor (.) never changes; seats don't move, and nobody sits on the floor.
	*/

	var smap_new *seatmap = make_seatmap(smap.height, smap.width)
	var coord Seat
	var num_adj_occupied int

	for h := 0; h < smap.height; h++ {
		for w := 0; w < smap.width; w++ {

			num_adj_occupied = 0
			seat_this := smap.seatmapstring[h][w]

			if a.queen_vision {

				for _, adjacent_coordinate := range a.adjacent_seats {
					coord.h = h
					coord.w = w
					// Check adjacent seat in direction of |adjacent_coordinate|.
					for {
						coord.h += adjacent_coordinate.h
						coord.w += adjacent_coordinate.w
						if coord.h >= smap.height || coord.h < 0 || coord.w >= smap.width || coord.w < 0 {
							// out of seatmap
							break
						}
						look_for_seat := smap.seatmapstring[coord.h][coord.w]
						if look_for_seat == '#' {
							// Adjacent seat is within range. Count it.
							num_adj_occupied += 1
							break
						}
						if look_for_seat == 'L' {
							break
						}
					}
				}
			} else {
				// Count number of occupied adjacent seats.
				for _, coordinate := range a.adjacent_seats {
					if (h+coordinate.h < smap.height && h+coordinate.h >= 0) && (w+coordinate.w < smap.width && w+coordinate.w >= 0) {
						adjacent_seat := smap.seatmapstring[h+coordinate.h][w+coordinate.w]
						if adjacent_seat == '#' {
							num_adj_occupied += 1
						}
					}
				}
			}

			// Assign new seat state according to seatmap logic.
			smap_new.seatmapstring[h][w] = next_seat(seat_this, num_adj_occupied, a.num_adj_occupied_tolerance)

		}
	}
	return *smap_new

}

// Get the number of occupied seats in a seatmap.
func num_occupied_seats(smap seatmap) int {
	var count int = 0
	for h := range smap.seatmapstring {
		for w := range smap.seatmapstring[h] {
			if smap.seatmapstring[h][w] == '#' {
				count += 1
			}
		}
	}
	return count
}

func run_sim(smap seatmap, sim_step_limit int, adjacent_seats []Seat, sf sim_func) {

	// Simulate seat popluation over time.
	var new_state *seatmap = make_seatmap(smap.height, smap.width)
	var old_state *seatmap = make_seatmap(smap.height, smap.width)
	var x int

	*old_state = smap

	for x := 0; x < sim_step_limit; x++ {
		*new_state = sf.get_next_state(old_state)
		if seatmap_equal(old_state, new_state) {
			break
		}
		*old_state = *new_state
	}
	fmt.Println("Simulation has reached steady state after " + fmt.Sprint(x) + " iterations.")
	fmt.Println("There are " + fmt.Sprint(num_occupied_seats(*new_state)) + " seats occupied.")

}

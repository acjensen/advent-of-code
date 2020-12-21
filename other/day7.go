// THE GO SOLUTION IS A WORK In PROGRESS

// take advantage of a compiled-language's compiler 'linker' and pointers to resolve this.
// https://stackoverflow.com/questions/8261058/invalid-recursive-type-in-a-struct-in-go
// a pointer is required because there is no way for the compiler to allocate memory for a recursive type, so
// it just points to the next type in the implicitly created 'list' structure...
// this makes languages with pointers much more... descriptive.

// The combination of recursive type definition may only be possible in python using a list in the "=" part of a class definition?

// in python, we couldn't be this descriptive with our types: we had to use a hashmap of tuples, where the hashmap keys were colors and the values were 'contains' relationship (edges of a graph)
// but, this might be an 'advantage' for some people... they don't have to think about types then.
// I think the code would be much less re-usable though

// basically.... use a pointer whenever you expect to have any sort of eventual type loopback / recursive relationship!!

package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
)

type void struct{}

// interesting... the choice between using set and a slice
type Bags map[*Bag]void

type Color struct {
	name string
}

type ContainsList []*Contains

type Bag struct {
	color         Color
	contains_list ContainsList
}

type Contains struct {
	amount int
	bag    Bag
}

func load_text(filename string) []string {
	file_as_one_big_string, _ := ioutil.ReadFile(filename)
	lines := regexp.MustCompile("\n").Split(string(file_as_one_big_string), -1)
	return lines
}

func deserialize(lines []string) Bags {
	// Maps a list of strings to a bunch of connected objects in memory.
	// This is difficult because we are mapping a list of edges (the input.txt)
	// to a recursive in-memory data structure. We're creating a network of objects
	// with pointers from the input.txt instead of just a map structure that relates
	// strings/ints.
	re1 := regexp.MustCompile(`([\w\s]*) bags contain ([\w\s,]*.)`)
	re2 := regexp.MustCompile(`(\d|no) ([\w\s]*) bags?[,.]`)

	bags := Bags{} // add size later?
	for _, line := range lines {
		fmt.Println(line)
		m := re1.FindStringSubmatch(line)
		bag := Bag{}
		fmt.Println(m)
		bag.color = Color{m[1]}
		subs := re2.FindAllStringSubmatch(m[2], -1)
		contains_list := make(ContainsList, len(subs))
		for i, c := range subs {
			contains := Contains{}
			if c[1] == "no" {
				contains.amount = 0
			} else {
				contains.amount, _ = strconv.Atoi(c[1])
			}
			contains.bag = Bag{Color{c[2]}, nil}
			contains_list[i] = &contains
		}
		bag.contains_list = contains_list
		bags[&bag] = void{}
	}
	return bags
}


func part1(bags Bags) nil {

	//  Reverse the 'rules dict' which is an adjacency list
	adjacency_list = defaultdict(list)
	for bag, contains in rules_dict.items():
	for c in contains:
	contains_num, contains_bag = c
	adjacency_list[contains_bag].append((bag, contains_num))
	
	# Depth First Search from starting node to all end nodes and marking whether the node is visited
	start_n = "shiny gold"
	visited = {key: False for key in adjacency_list.keys()}
	
	def depth_first_search(n):
	# Reached a bag that is not 'contained' by any other bag.
	if n not in adjacency_list:
	visited[n] = True
	else:
	if not visited[n]:
	visited[n] = True
	for m_name, _ in adjacency_list[n]:
	depth_first_search(m_name)
	
	depth_first_search(start_n)
	
	# The answer is the sum of the visited bags.
	num_bags_visited = sum([1 for _, value in visited.items() if value])
	# don't count the shiny bag itself as an option - it must be carried by another bag.
	num_bags_visited -= 1
	
	print(f'Part 1: {num_bags_visited}')
}



func main() {
	fmt.Println("lol")
	mybag := Bag{Color{"yellow"}, nil}
	fmt.Println(mybag.color.name)
	contains_ptr := &Contains{1, mybag}
	myslice := []*Contains{contains_ptr}
	mybag2 := Bag{Color{"silver"}, myslice}
	fmt.Println(mybag2.color.name)
	mybag2_child_bag := *(mybag2.contains_list[0])
	fmt.Println(mybag2_child_bag.bag.color.name)

	pwd, _ := os.Getwd()
	text := load_text(filepath.Join(pwd, "/day7/input.txt"))
	bags := deserialize(text)
	fmt.Println(bags)
}

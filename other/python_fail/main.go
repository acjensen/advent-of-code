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
)

type color struct {
	name string
}

type bag struct {
	color    color
	contains *contains // critical pointer here
}

type contains struct {
	amount int
	bag    bag
}

func main() {
	fmt.Println("lol")
	mybag := bag{color{"yellow"}, nil}
	fmt.Println(mybag.color.name)
	mybag2 := bag{color{"silver"}, &contains{1, mybag}}
	fmt.Println(mybag2.color.name)
	mybag2_child_bag := *(mybag2.contains)
	fmt.Println(mybag2_child_bag.bag.color.name)
}

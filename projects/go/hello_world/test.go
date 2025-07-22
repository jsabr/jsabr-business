package main

import "fmt"

func main() {
	x := 10
	ptr := &x // &x gives the address of x

	fmt.Println("x:", x)       // 10
	fmt.Println("ptr:", ptr)   // memory address like 0xc000012030
	fmt.Println("*ptr:", *ptr) // dereference: 10

	*ptr = 20                            // change x through the pointer
	fmt.Println("x after *ptr = 20:", x) // 20
}

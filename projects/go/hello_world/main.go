package main

import (
	"flag"
	"fmt"
	"os"
)

// greet prints a greeting message
func greet(name string) {
	fmt.Printf("Hello, %s! Welcome to Go.\n", name)
}

func main() {
	// Define a flag to accept a name from the command line
	name := flag.String("name", "World", "Name to greet")
	flag.Parse()

	// Handle empty name or other basic logic
	if *name == "" {
		fmt.Fprintln(os.Stderr, "Error: name cannot be empty.")
		os.Exit(1)
	}

	greet(*name)
}

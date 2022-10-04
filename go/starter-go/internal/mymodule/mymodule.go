package mymodule

import "fmt"

// ReturnTwo should return 2
func ReturnTwo() (int, error) {
	fmt.Println("Remember to put your Go directory into proper GOPATH")
	return 2, nil
}

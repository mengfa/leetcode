package main

import (
	"fmt"
	"os"
)

// func main() {
// 	fmt.Println("Hello World")
// }
//

func main() {
	if len(os.Args) > 1 {
		fmt.Println("Hello World", os.Args[1])
	}
}

package fib

import (
	"fmt"
	"testing"
)

// func TestFibList(t *testing.T) {
// 	var a int = 1
// 	var b int = 1
// 	fmt.Print(a)
// 	for i := 0; i < 5; i++ {
// 		fmt.Print(" ", b)
// 		tmp := a
// 		a = b
// 		b = tmp + a
// 	}
// 	fmt.Println()
// 	t.Log("1")
// 	t.Log("1")
// }
//
// func TestExchange(t *testing.T) {
// 	a := 1
// 	b := 2
//
// 	a, b = b, a
// 	fmt.Println(a, b)
// 	t.Log("11111")
// 	t.Log(a, b)
// }
func TestConst(t *testing.T) {
	const (
		Monday = iota + 1
		Tuesday
		Wednesday
		Thursday
		Friday
		Saturday
		Sunday
	)
	const (
		Open = 1 << iota
		Close
		Pending
	)
	fmt.Println(Tuesday)
	fmt.Println(Pending)
}

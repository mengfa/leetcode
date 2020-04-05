package fib

import (
	"fmt"
	"testing"
)

func TestFibList(t *testing.T) {
	var a int = 1
	var b int = 1
	fmt.Print(a)
	for i := 0; i < 5; i++ {
		fmt.Print(" ", b)
		tmp := a
		a = b
		b = tmp + a
	}
	fmt.Println()
	t.Log("1")
	t.Log("1")
}

func TestExchange(t *testing.T) {
	a := 1
	b := 2

	a, b = b, a
	t.Log(a, b)
}

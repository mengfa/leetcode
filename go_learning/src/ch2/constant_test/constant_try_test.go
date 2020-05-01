package constant_test

import (
	"fmt"
	"testing"
)

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
	Readable = 1 << iota
	Writable
	Executable
)

func TestConstantTry(t *testing.T) {
	a := 1
	fmt.Println(a & Readable)
	fmt.Println(a & Writable)
	fmt.Println(a & Executable)
	fmt.Println(Readable)
	fmt.Println(Writable)
	fmt.Println(Executable)
	fmt.Println(a&Readable == Readable)
	fmt.Println(a&Writable == Writable)
	fmt.Println(a&Executable == Executable)
}

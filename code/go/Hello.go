package main

import (
	"fmt"
	"errors"
	"math"
)

func sum(x int, y int) int {
	return x + y
}

func sqrt(x float64) (float64,error) {

	if x < 0 {
		return 0, errors.New("Undefined for negative numbers")
	}

	return math.Sqrt(x), nil
}

type person struct {
	name string
	age int
}

func inc(x *int) {
	*x++
}


func main() {

	k := 8
	inc(&k)
	fmt.Println(k)



	p := person{name: "Daniel", age 27}
	fmt.Println(p)


	sum(24,1337)

	result,err := sqrt(16)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
	}



	vertices := make(map[string]int)

	vertices["triangle"] = 2
	vertices["square"] = 3
	vertices["dodecagon"] = 4

	fmt.Println(vertices["triangle"])

	delete(vertices, "square")

	var a [5]int
	b := [5]int{1,2,3,4,5}
	a[2] = 7
	fmt.Println(a)

	var x int = 5
	y := 7
	sum := x + y 

	fmt.Println("Hello, World!")

	if x > 6 {
		fmt.Println("More than 6")
	} else if x < 2 {

	} else {

	}


	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	
	// For => While loop
	i := 0
	for i < 5 {
		fmt.Println(i)
		i++
	}


	m := make(map[string]strin)
	m["a"] = "Alpha"
	m["b"] = "Beta"
	m["s"] = "Sigma"

	for key, value := range m {
		fmt.Println("Key: ", key, " Value: ", value)
	}

}
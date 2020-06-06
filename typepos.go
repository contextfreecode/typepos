package main

import "fmt"

type orderLine struct {
	UnitPrice float64
	Quantity  int
}

type namedOrderLine struct {
	orderLine
	Name string
}

func totalPrice(lines []orderLine) float64 {
	sum := 0.0
	for _, line := range lines {
		sum += line.UnitPrice * float64(line.Quantity)
	}
	return sum
}

func main() {
	var line interface{} = orderLine{UnitPrice: 0.25, Quantity: 2}
	order := []orderLine{
		line.(orderLine),
		{UnitPrice: 1.00, Quantity: 1},
	}
	fmt.Println(totalPrice(order))
}

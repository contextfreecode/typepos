import Foundation

struct OrderLine {
    var unitPrice: Decimal
    var quantity: Int
}

func totalPrice(lines: AnySequence<OrderLine>) -> Decimal {
    return lines.reduce(into: Decimal(0)) { total, line in
        total += line.unitPrice * Decimal(line.quantity)
    }
}

func main() {
    let line: Any = OrderLine(unitPrice: 0.25, quantity: 2)
    let order = [
        // Though pattern matching better in some of these languages.
        line as! OrderLine,
        OrderLine(unitPrice: 1.00, quantity: 1),
    ]
    print(totalPrice(lines: AnySequence(order)))
}

main()

class OrderLine(
    var unitPrice: Double,
    var quantity: Int
)

fun totalPrice(lines: Iterable<OrderLine>): Double {
    return lines.fold(0.0, { total, line ->
        total + line.unitPrice * line.quantity
    })
}

fun main() {
    val line: Any = OrderLine(unitPrice = 0.25, quantity = 2)
    val order = listOf(
        line as OrderLine,
        OrderLine(unitPrice = 1.00, quantity = 1)
    )
    println(totalPrice(order))
}

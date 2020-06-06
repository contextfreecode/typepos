class OrderLine(
  var unitPrice: BigDecimal,
  var quantity: Int,
);

object TypePos {
  def totalPrice(lines: Iterable[OrderLine]): BigDecimal = {
    lines.foldLeft(BigDecimal(0)) ((total, line) =>
      total + line.unitPrice * line.quantity
    )
  }

  def main(args: Array[String]) {
    val line: Object = new OrderLine(unitPrice = 0.25, quantity = 2)
    val order = Array(
      line.asInstanceOf[OrderLine],
      new OrderLine(unitPrice = 1.00, quantity = 1),
    )
    println(totalPrice(order))
  }
}

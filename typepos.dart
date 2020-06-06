class OrderLine {
  double unitPrice;
  int quantity;
  OrderLine({this.unitPrice, this.quantity});
}

double totalPrice(Iterable<OrderLine> lines) {
  return lines.fold(0, (total, line) => total + line.unitPrice * line.quantity);
}

main() {
  Object line = OrderLine(unitPrice: 0.25, quantity: 2);
  var order = [
    line as OrderLine,
    OrderLine(unitPrice: 1.00, quantity: 1),
  ];
  print(totalPrice(order));
}

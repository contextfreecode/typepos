interface OrderLine {
  unitPrice: number;
  quantity: number;
}

function totalPrice(lines: Iterable<OrderLine>): number {
  let total = 0;
  for (let line of lines) {
    total += line.unitPrice * line.quantity;
  }
  return total;
  // return lines.reduce(
  //   (total, line) => total + line.unitPrice * line.quantity,
  //   0,
  // );
}

function main() {
  let line: unknown = { unitPrice: 0.25, quantity: 2 };
  let order: OrderLine[] = [
    // <OrderLine> line,
    line as OrderLine,
    { unitPrice: 1.00, quantity: 1 },
  ];
  console.log(totalPrice(order));
}

main()

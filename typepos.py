from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable, List, cast


@dataclass
class OrderLine:
    unit_price: Decimal
    quantity: int


@dataclass
class NamedOrderLine(OrderLine):
    name: str


def total_price(lines: Iterable[OrderLine]) -> Decimal:
    line_totals = (line.unit_price * line.quantity for line in lines)
    return sum(line_totals, Decimal("0"))


def main():
    line: object = OrderLine(unit_price=Decimal("0.25"), quantity=2)
    order: List[OrderLine] = [
        cast(OrderLine, line),
        OrderLine(unit_price=Decimal("1.00"), quantity=1),
    ]
    print(total_price(order))


if __name__ == "__main__":
    main()

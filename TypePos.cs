using System;
using System.Collections.Generic;
using System.Linq;

class OrderLine {
    public decimal UnitPrice;
    public int Quantity;
}

class TypePos {
    // static decimal TotalPrice<Item>(IEnumerable<Item> lines)
    //         where Item : OrderLine {
    static decimal TotalPrice(IEnumerable<OrderLine> lines) {
        return lines.Aggregate(
            0m, (total, line) => total + line.UnitPrice * line.Quantity
        );
    }

    static void Main() {
        var line = (object)new OrderLine {UnitPrice = 0.25m, Quantity = 2};
        var order = new [] {
            line as OrderLine,
            new OrderLine {UnitPrice = 1.00m, Quantity = 1},
        };
        Console.WriteLine(TotalPrice(order));
    }
}

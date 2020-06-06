import java.math.*;
import java.util.*;
import java.util.stream.*;

class OrderLine {
    BigDecimal unitPrice;
    int quantity;
    OrderLine(BigDecimal unitPrice, int quantity) {
        this.unitPrice = unitPrice;
        this.quantity = quantity;
    }
}

class TypePos {
    static BigDecimal totalPrice(Iterable<OrderLine> lines) {
        return StreamSupport.stream(lines.spliterator(), false)
            .map(line -> line.unitPrice.multiply(new BigDecimal(line.quantity)))
            .reduce(BigDecimal.ZERO, (a, b) -> a.add(b));
    }

    public static void main(String[] args) {
        Object line = new OrderLine(new BigDecimal("0.25"), 2);
        var order = Arrays.asList(
            (OrderLine)line,
            new OrderLine(new BigDecimal("1.00"), 1)
        );
        System.out.println(totalPrice(order));
    }
}

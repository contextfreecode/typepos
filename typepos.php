<?php

declare(strict_types=1);

class OrderLine {
    public float $unitPrice;
    public int $quantity;
    function __construct(float $unitPrice, int $quantity) {
        $this->unitPrice = $unitPrice;
        $this->quantity = $quantity;
    }
}

// function totalPrice(OrderLine ...$lines): float {
function totalPrice(iterable $lines): float {
    $total = 0;
    foreach ($lines as $line) {
        $total += $line->unitPrice * $line->quantity;
    }
    return $total;
}

function main() {
    // $line = (object) ['unitPrice' => 0.25, 'quantity' => 2];
    // See also: https://wiki.php.net/rfc/named_params
    $order = [new OrderLine(0.25, 2), new OrderLine(1.0, 1)];
    printf("%.2f\n", totalPrice($order));
    // printf("%.2f\n", totalPrice(...$order));
}

main();

?>

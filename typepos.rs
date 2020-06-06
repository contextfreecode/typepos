use std::any::*;

#[derive(Clone, Copy)]
struct OrderLine {
    unit_price: f64,
    quantity: isize,
}

fn total_price(lines: &mut dyn Iterator<Item = &OrderLine>) -> f64 {
    lines.fold(0.0, |total, line| {
        total + line.unit_price * line.quantity as f64
    })
}

fn main() {
    let line: &dyn Any = &OrderLine{unit_price: 0.25, quantity: 2};
    let order = [
        *line.downcast_ref::<OrderLine>().unwrap(),
        OrderLine{unit_price: 1.00, quantity: 1},
    ];
    println!("{:.2}", total_price(&mut order.iter()));
}

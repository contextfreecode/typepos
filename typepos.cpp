#include <any>
#include <iostream>
#include <numeric>
#include <vector>

using Decimal = double;
// typedef double Decimal;

struct OrderLine {
  Decimal unit_price;
  double quantity;
};

// template<LinesConcept Lines>
template<typename Lines>
// decltype(std::begin(lines)->unit_price)
// decltype(Lines::value_type::unit_price)
auto total_price(const Lines& lines)
  -> decltype(std::begin(lines)->unit_price)
  // -> decltype(Lines::value_type::unit_price)
{
  using UnitPrice = decltype(std::begin(lines)->unit_price);
  return std::accumulate(
    lines.begin(), lines.end(), UnitPrice(0.0),
    [&](UnitPrice total, const OrderLine& line) {
      return total + line.unit_price * line.quantity;
    }
  );
}

auto main() -> int {
  auto line = std::any(OrderLine {.unit_price = 0.25, .quantity = 2});
  auto lines = std::vector<OrderLine> {
    std::any_cast<OrderLine>(line),
    {.unit_price = 1.00, .quantity = 1},
  };
  std::cout << total_price(lines) << std::endl;
}

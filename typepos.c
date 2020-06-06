#include <stdio.h>

typedef struct OrderLine {
  double unit_price;
  int quantity;
} OrderLine;

double total_price(OrderLine lines[], size_t lines_length) {
  double total = 0;
  for (size_t i = 0; i < lines_length; i += 1) {
    total += lines[i].unit_price * lines[i].quantity;
  }
  return total;
}

int main() {
  void* line = &(OrderLine){.unit_price = 0.25, .quantity = 2};
  OrderLine order[] = {
    *(OrderLine*)line,
    {.unit_price = 1.00, .quantity = 1},
  };
  printf("%.2f\n", total_price(order, sizeof(order) / sizeof(*order)));
}

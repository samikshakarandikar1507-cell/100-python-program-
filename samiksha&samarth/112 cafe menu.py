item1, price1 = "Coffee", 3.50
item2, price2 = "Bagel", 2.25
width=12
print("="*6 +f"{' RECEIPT '}" + '='*6)
#print("-"*(width+9))
print(f"{item1:<{width}}{'$':>4}{price1:>5.2f}")
print(f"{item2:<{width}}{'$':>4}{price2:>5.2f}")
print("-"*(width+9))
Total= price1+price2
print(f"Total          ${Total:>5.2f}")

import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check_output("====== RECEIPT ======\nCoffee         $ 3.50\nBagel          $ 2.25\n---------------------\nTotal          $ 5.75", hint="f\"{' RECEIPT ':=^21}\" gives the title bar; f\"{item1:<15}${price1:>5.2f}\" gives a line.")

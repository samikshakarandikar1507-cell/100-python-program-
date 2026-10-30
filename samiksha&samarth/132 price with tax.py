price = float(input("Enter the price: "))
tax_rate = float(input("Enter the tax rate in percent: "))

total = price + (price * tax_rate / 100)

print(f"Total: {total:.2f}")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("Total: 86.00", inputs=["80", "7.5"])

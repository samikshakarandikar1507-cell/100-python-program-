price = 10
quantity = 3
total = price * quantity
price = 20
quantity = quantity + 1

total_after = total
new_total =price * quantity
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(total_after, 30)
check(new_total, 80)



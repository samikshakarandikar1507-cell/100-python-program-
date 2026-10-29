sweets = 17
children = 5

each = sweets//children
left_over = sweets%children
print(each)
print(left_over)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(each, 3)
check(left_over, 2)

raw_a="12"
raw_b="30"
total=int(raw_a)+int(raw_b)
joined=str(raw_a)+(raw_b)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(total, 42)
check(joined, "1230")

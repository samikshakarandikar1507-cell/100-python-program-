s = "abcdefghi"

middle = s[len(s)//2]

outer_removed = s[1:-1]
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(middle, "e")
check(outer_removed, "bcdefgh")

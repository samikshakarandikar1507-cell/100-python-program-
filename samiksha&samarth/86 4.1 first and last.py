word = "Python"
first = (word[0])
last = (word[-1])
first_three =(word[:3])
last_three = (word[-3:])
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(first, "P")
check(last, "n")
check(first_three, "Pyt")
check(last_three, "hon")

two_lines="Line one\nLine two"
columns="A\tB\tC"
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(two_lines, "Line one\nLine two")
check(columns, "A\tB\tC")

typo = "Pxthon"

fixed = typo[:1]+"y"+typo[2:]
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(fixed, "Python")

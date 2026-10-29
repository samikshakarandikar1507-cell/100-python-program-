text = "stressed"

reversed_text =(text[::-1])
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(reversed_text, "desserts")

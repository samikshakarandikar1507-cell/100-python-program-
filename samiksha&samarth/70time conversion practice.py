total_seconds=98765
hours=total_seconds//3600
minutes=(total_seconds%3600)//60
seconds=total_seconds%60
print(hours)
print(minutes)
print(seconds)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(hours, 27)
check(minutes,26)
check(seconds,5)

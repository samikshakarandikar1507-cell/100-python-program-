minutes = int(input("Enter the number of minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutes = {hours} h {remaining_minutes} min")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("135 minutes = 2 h 15 min", inputs=["135"])



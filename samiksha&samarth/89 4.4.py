date = "2026-10-18"

year = date[:4]
month = date[5:7]
day = date[8:10]
uk_date = day+"/"+month+"/"+year
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(year, "2026")
check(month, "10")
check(day, "18")
check(uk_date, "18/10/2026")

alphabet = "abcdefghijklmnopqrstuvwxyz"

every_other = alphabet[::2]
last_five_reversed = alphabet[:20:-1]
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

check(every_other, "acegikmoqsuwy")
check(last_five_reversed, "zyxwv")

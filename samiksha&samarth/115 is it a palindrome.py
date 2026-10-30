phrase = "A man, a plan, a canal: Panama"

cleaned = phrase.lower().replace(" ","").replace(",","").replace(":","")
is_palindrome=cleaned==cleaned[::-1]
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(cleaned, "amanaplanacanalpanama")
check(is_palindrome, True)


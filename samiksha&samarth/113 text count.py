text = "the cat and the hat and the bat"

word_count =text.split().__len__()
the_count = text.count("the")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(word_count, 8)
check(the_count, 3)

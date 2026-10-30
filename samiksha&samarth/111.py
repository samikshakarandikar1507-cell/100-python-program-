headline = "the quick brown fox"

slug=headline.replace(" ","-")
title = headline.title()
acronym = (headline.split()[0][0]+headline.split()[1][0]+headline.split()[2][0]+headline.split()[3][0]).upper()
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(slug, "the-quick-brown-fox")
check(title, "The Quick Brown Fox")
check(acronym, "TQBF")

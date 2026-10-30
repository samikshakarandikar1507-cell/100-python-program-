name = input("What is your name? ")
print("Hello, " + name + "!")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("Hello, Ada!", inputs=["Ada"])

print("*"*10)
print("*"+" "*8+"*")
print("*  Hi!  *")
print("*" + " "*8 +"*")
print("*"*10)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("**********\n*        *\n*  Hi!   *\n*        *\n**********")

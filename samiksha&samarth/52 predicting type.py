t1= 7
t2= 7.0
t3="7"
t4=7>4
t5=3+4.5
t1 = "int"
t2 = "float"
t3 = "str"
t4 = "bool"
t5 = "float"
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(t1, "int")
check(t2, "float")
check(t3, "str")
check(t4, "bool")
check(t5, "float")

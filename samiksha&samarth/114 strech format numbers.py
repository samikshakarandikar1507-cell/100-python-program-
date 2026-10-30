amount = 1234567.891
share = 0.4567
user_id = 42
number = 10

 
money= (f"{1234567.891:,.2f}")      
percent=(f"{0.4567:.1%}")
padded_id=(f"{42:06d}")       
binary=(f"{10:b}")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(money, "1,234,567.89")
check(percent, "45.7%")
check(padded_id, "000042")
check(binary, "1010")


 

 

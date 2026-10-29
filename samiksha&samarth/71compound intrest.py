principal=1000
rate_percent=5
years=10
amount=round(principal*(1+rate_percent/100)**years,2)
balance=1000
balance*=1.05
balance*=1.05
balance*=1.05
print(amount)
print(balance)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(amount,1628.89)
check(balance, 1157.625, tol=1e-6)

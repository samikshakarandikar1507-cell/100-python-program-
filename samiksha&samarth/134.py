num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3
print(f"Average: {average:.2f}")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("Average: 2.33", inputs=["1", "2", "4"])

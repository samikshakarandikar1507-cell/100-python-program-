weight = float(input("Your weight in kilograms: "))
height = float(input("Your height in metres: "))

BMI = weight / height ** 2

print(f"Your BMI is {BMI:.1f}")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("Your BMI is 22.9", inputs=["70", "1.75"])

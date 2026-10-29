import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
planet = "Mars"
moons = 2
print(planet)
print(planet, "has", moons, "moons")
check(planet, "Mars")
check(moons, 2)

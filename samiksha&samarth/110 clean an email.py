raw_email = "  JOHN.SMITH@Example.COM \n"

email = raw_email.strip().lower()
username = raw_email.strip("@Example.COM \n").lower()
domain = email.split("@")[1]
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(email, "john.smith@example.com")
check(username, "john.smith")
check(domain, "example.com")

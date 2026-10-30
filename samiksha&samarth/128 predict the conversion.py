c1=int(3.99)
c2=float("2")
c3=str(7)+str(7)
c4=bool("")
c5=bool("0")
c6=int("42")+float("0.5")
for name, value in[
    ("c1", c1),
    ("c2", c2),
    ("c3", c3),
    ("c4", c4),
    ("c5", c5),
    ("c6", c6)
]:
    print(name, "=", value, "| Type:", type(value).__name__)

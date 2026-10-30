price=float(input("Enter the price:"))
tax_rate=float(input("Enter the tax rate in percent:"))
total=price+(price*tax_rate/100)
print(f"Total:{total:.2f}")

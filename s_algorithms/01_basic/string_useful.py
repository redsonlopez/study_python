hedson= "hEdSon"
aline= "  Aline   "

print(hedson.upper())
print(hedson.lower())
print(hedson.title())

print()

print(aline + ".")
print(aline.strip() + ".")
print(aline.rstrip() + ".") # right strip
print(aline.lstrip() + ".") # left strip

print()

print(hedson.center(10, "#"))
print(".".join(hedson))


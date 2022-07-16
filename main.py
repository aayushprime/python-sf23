# this is how you import a from standard lib module
import sys

from fraction import Fraction

print(sys.version_info)

a = Fraction(2, 3)
b = Fraction(3, 4)

c = a + b
print(c)

try:
    d = Fraction(1, 0)
    print("fraction d created")
except:
    print("Exception occured")

import re
import cmath

s = input().strip()
regex = r'(-?\d+)([\+-]\d+)j'
z = re.match(regex, s)
real, img = int(z.group(1)), int(z.group(2))

r, pi = cmath.polar(complex(real, img))
print(r)
print(pi)

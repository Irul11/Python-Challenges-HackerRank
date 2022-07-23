import math

ab = int(input())
bc = int(input())

hyp = math.sqrt(ab**2 + bc**2)
cos_c = bc/hyp
sin_c = ab/hyp
mc = hyp/2
cd = cos_c*mc
dm = math.sqrt(mc**2 - cd**2)
b = math.atan(dm/(bc-cd))
print(str(round(math.degrees(b))) + chr(176))
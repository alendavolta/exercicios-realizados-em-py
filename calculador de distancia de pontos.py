import math
a = float(input("x1"))
b = float(input("y1"))
c = float(input("x2"))
d = float(input("y2"))

distancia = math.sqrt((a-b)**2+(c-d)**2)

if distancia >=10:
         print ("longe")
else: print ("perto")
         

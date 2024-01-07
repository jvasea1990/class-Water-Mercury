from experiment_water import *
from experiment_water import object_print
print ()

w1=Water ("little_water", 1, "100")
w2=Water ("big_water", "5", -150)
m1=Mercury ("little_mercury", 2, -40)

print ()
m1+w1

object_print (w1)
object_print(m1)

w2.state()
print ()
import model
import motor
from constants import *


print("_________Test dk_________")

m= model.Model()
m.m1.speed = 10
m.m2.speed = 10
print("First Model:{}".format(m))


linear_speed, rotational_speed = m.dk(m1_speed=10, m2_speed=10)
print("\n#####\nmodel: {}".format(m))
if linear_speed == 10 and rotational_speed == 0:
    print("Test with same speeds OK")
else:
    print("Test with same speeds : You suck!")


m= model.Model()
m.m1.speed = -10
m.m2.speed = 10
print("Second Model:{}".format(m))


linear_speed, rotational_speed = m.dk(m1_speed=-10, m2_speed=10)
print("\n#####\nmodel: {}".format(m))
if linear_speed == 0 and rotational_speed == -20/model.l:
    print("Test with opposite speeds OK")
else:
    print("Test with opposite speeds : You suck!")


m= model.Model()
m.m1.speed = 0
m.m2.speed = 10
print("Second Model:{}".format(m))


linear_speed, rotational_speed = m.dk(m1_speed=-10, m2_speed=10)
print("\n#####\nmodel: {}".format(m))
if linear_speed == 5 and rotational_speed == -10/m.l:
    print("Test with different speeds OK")
else:
    print("Test with different speeds : You suck!")


print("_________Test ik_________")

linear_speed, rotational_speed = m.dk(m1_speed=-10, m2_speed=10)
print("\n#####\nmodel: {}".format(m))
if linear_speed == 5 and rotational_speed == -10/m.dt:
    print("Test with different speeds OK")
else:
    print("Test with different speeds : You suck!")
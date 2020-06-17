# bounce.py
#
# Exercise 1.5
height = 100
bounce = 0

while (bounce < 10):
    height = height * 3 / 5
    bounce = bounce + 1
    print (bounce, round(height, 4))
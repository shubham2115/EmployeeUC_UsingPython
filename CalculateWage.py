import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
attendance = random.randint(0, 1)
if attendance == 1:
    print("Employee is present")
    totalWage = WAGE_PER_HOUR * FULL_DAY_HOUR
    print("Total wage is ", totalWage)
else:
    print("Employee is absent")
    print("Total wage is 0")
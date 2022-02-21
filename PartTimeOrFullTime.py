import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
attendance = random.randint(0, 2)
if attendance == 1:  # to check employee is present
    print("Employee is present")
    totalWage = WAGE_PER_HOUR * FULL_DAY_HOUR
    print("Total wage is ", totalWage)
elif attendance == 2:  # to check employee is part-time present
    print("Employee present for PartTime")
    partTimeWage = WAGE_PER_HOUR * PART_TIME_HOUR
    print("Part time wage is ", partTimeWage)
else:
    print("Employee is absent")
    print("Total wage is 0")
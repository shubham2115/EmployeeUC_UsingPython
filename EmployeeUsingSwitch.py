import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
_wage = {
    0: {'attendance': 'absent', 'wage': 0, 'worked_hr': 0},
    1: {'attendance': 'present', 'wage': WAGE_PER_HOUR, 'worked_hr': FULL_DAY_HOUR},
    2: {'attendance': 'part-time', 'wage': WAGE_PER_HOUR, 'worked_hr': PART_TIME_HOUR}
}
attendance = random.randint(0, 2)
print("wage according to Attendace is", _wage.get(attendance))
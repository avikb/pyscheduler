import sys
from scheduler import PriorityScheduler


shed = PriorityScheduler(
    [1, 2, 3],
    [
        PriorityScheduler([1, 2, 3], ["a1", "a2", "a3"]),
        PriorityScheduler([1, 2], ["b1", "b2"]),
        PriorityScheduler([1], ["c1"])
    ]
)

for i in range(int(sys.argv[1])):
    print(shed.next().next())

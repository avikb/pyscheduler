import sys
from scheduler import PriorityScheduler
from scheduler import Scheduler


shed = PriorityScheduler(
    [1, 2, 3],
    [
        Scheduler(["a1", "a2", "a3"]),
        PriorityScheduler([1, 2], ["b1", "b2"]),
        Scheduler(["c1"])
    ]
)

for i in range(int(sys.argv[1])):
    print(shed.next().next())

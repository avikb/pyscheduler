import sys
from scheduler import PriorityScheduler
from scheduler import Scheduler


shed = PriorityScheduler(
    [
        Scheduler(["a1", "a2", "a3"]),
        PriorityScheduler(["b1", "b2"], [1, 2]),
        Scheduler(["c1"])
    ],
    [1, 2, 3]
)

for i in range(int(sys.argv[1])):
    print(shed.next().next())

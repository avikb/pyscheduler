class Scheduler:
    def __init__(self, list):
        self.__list = list
        self.__ind = 0

    def next(self):
        current = self.__ind
        self.__ind += 1
        if self.__ind == len(self.__list):
            self.__ind = 0
        return self.__list[current]


class PriorityScheduler:
    def __init__(self, list, priorities):
        if len(priorities) != len(list):
            raise Exception('bad usage')
        self.__list = list
        self.__priorities = priorities
        self.__counters = self.__priorities[:]
        self.__ind = 0

    def next(self):
        while True:
            current = self.__ind
            # rotate list pointer
            self.__ind += 1
            if self.__ind == len(self.__list):
                self.__ind = 0
            # is object ready?
            self.__counters[current] -= 1
            if self.__counters[current] == 0:
                # print(self.__counters)
                self.__counters[current] = self.__priorities[current]
                return self.__list[current]

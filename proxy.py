class ProxyManager:
    def __init__(self, proxies):
        self.__ind = 0
        self.__proxies = proxies
        self.__busy = [False] * len(self.__proxies)

    def get(self):
        if self.__busy.count(False) == 0:
            return None
        if self.__ind > len(self.__busy):
            self.__ind = 0
        current = None
        try:
            current = self.__busy.index(False, self.__ind)
        except ValueError:
            current = self.__busy.index(False, 0, self.__ind - 1)
        self.__ind = current + 1
        self.__busy[current] = True
        return self.__proxies[current]

    def release(self, proxy):
        ind = self.__proxies.index(proxy)
        if self.__busy[ind] is not True:
            raise Exception('proxy wasn\'t in busy state')
        self.__busy[ind] = False

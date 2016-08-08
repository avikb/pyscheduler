import sys
import json
import threading

from scheduler import Scheduler
from scheduler import PriorityScheduler
from proxy import ProxyManager


class ObjectStringIterator:
    def __init__(self, objectsDict, prioritiesDict):
        defPriorityCnt = []
        objects = []
        for o in objectsDict:
            defPriorityCnt.append(prioritiesDict[o['priority']])
            objects.append({'taskSheduler': Scheduler(o['task']), 'info': o})
        self.__objects = PriorityScheduler(defPriorityCnt, objects)

    def next(self):
        o = self.__objects.next()
        return o['info'], o['taskSheduler'].next()


# main code

with open('data.json', 'r') as file:
    data = json.loads(file.read())


def siteWorker(site, priorities, objects, proxies, tries):
    ti = ObjectStringIterator(objects, priorities)
    pm = ProxyManager(proxies)

    for i in range(0, tries):
        proxy = pm.get()
        if proxy is None:
            break
        obj, task = ti.next()
        # print(site, task, proxy)
        print(task + ' -> ' + proxy['ip'] + ' => ' + site['domain'])
        # print(task)
        pm.release(proxy)


workers = []

for site in data['site']:
    worker = threading.Thread(
        target=siteWorker,
        args=(
            site,
            data['priorities'],
            data['object'],
            data['proxy'],
            int(sys.argv[1])
            )
        )
    workers.append(worker)
    worker.start()
    break

for worker in workers:
    worker.join()

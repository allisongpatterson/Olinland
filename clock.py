
class Clock (object):

    def __init__ (self,time):
        self._registry = {}
        self._time = time

    def register (self, f, priority):
        if priority in self._registry:
            self._registry[priority].append(f)
        else:
            self._registry[priority] = [f]

    def tick (self):
        self._time += 1
        keys = sorted(self._registry)
        for priority in keys:
            for event in self._registry[priority]:
                event(self._time)
                
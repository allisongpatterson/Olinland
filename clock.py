
class Clock (object):

    def __init__ (self,time):
        self._registry = {}
        self._time = time

    def register (self, f, priority):
        if self._registry[priority]:
            self._registry[priority].append(f)
        else:
            self._registry[priority] = [f]

    def tick (self):
        self._time += 1
        # Go through all functions in registry by priority
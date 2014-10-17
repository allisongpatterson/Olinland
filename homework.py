from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._done = False

    def is_homework (self):
        return True

    def is_done (self):
        return self._done

    def do_hw (self):
        self._done = True
        self._name = 'done-' + self._name

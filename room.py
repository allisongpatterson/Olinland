from wobject import *
from player import *
import random

class Room (WObject): #,Container):

    rooms = []

    # def __init__ (self,name,desc):
    def __init__ (self,name,desc,lockable):
        WObject.__init__(self,name)
        self._description = desc
        self._exits = {}
        self._contents = []
        Room.rooms.append(self)
        self._locked = False
        self._lockable = lockable
        if lockable:
            self._locked = True
            self._lock_timer = 3
            Player.clock.register(self.open_hours, 0)

    def description (self):
        return self._description

    def exits (self):
        return self._exits

    def contents (self):
        return self._contents

    def open_hours (self, time):
        self._lock_timer -= 1
        if not self._lock_timer:
            self._locked = not self._locked
            self._lock_timer = 3
            if self._locked:
                occupants = [x for x in self.contents() if x.is_person()]
                if occupants:
                    names = [x.name() for x in occupants]
                    occupants[0].location().report(self.name()+' closed and kicked out '+', '.join(names))
                    exits = self.exits()
                    dirc = random.choice(self.exits().keys())
                    for person in occupants:
                        person.go(dirc)


    # You see room reports only if you are in the same room
    # or if you have enabled god mode

    def report (self,msg):
        if Player.me.location() is self:
            print msg
        elif Player.god_mode:
            print '(At', self.name(), msg+')'

    def broadcast (self,msg):
        print msg

    def is_room (self):
        return True

    def is_locked (self):
        return self._locked

    def is_lockable (self):
        return self._lockable

    def have_thing (self,t):
        for c in self.contents():
            if c is t:
                return True
        return False

    def add_thing (self,t):
        self._contents.append(t)

    def del_thing (self,t):
        self._contents = [x for x in self._contents if x is not t]

import random
from npc import *

class Cat (NPC):

    def __init__ (self,name,loc,desc):
        Person.__init__(self,name,loc,desc)

        self._friend = None
        # Register proactive behaviors
        # Player.clock.register(self.follow, 3)

    def accept (self,obj,source):
        if obj.is_food():
            self.location().report(self.name() + ' takes the food and purrs loudly')
            obj.destroy()
            self._friend = source
            Player.clock.register(self.follow, 4)
        else:
            self.location().report(self.name() + ' has no use for that')

    def follow (self,time):
        loc = self.location()
        if self._friend and not self._friend.is_in_limbo():
            target = self._friend.location()
            if loc != target:
                target.report(self.name() + ' follows ' + self._friend.name() + ' to ' + target.name())
                loc.report(self.name() + ' follows ' + self._friend.name() + ' to ' + target.name())
                self.move(target)
        else:
            self._friend = None



    def die (self):
        self.say(':( :( :( :( :(')
        Person.die(self)

    def is_cat (self):
        return True
        
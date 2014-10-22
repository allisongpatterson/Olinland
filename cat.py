import random
from npc import *

class Cat (NPC):

    def __init__ (self,name,loc,desc):
        Person.__init__(self,name,loc,desc)

        self._friend = None
        # Register proactive behaviors
        # Player.clock.register(self.follow, 4)

    def accept (self,obj,source):
        if obj.is_food():
            self.location().report(self.name() + ' takes the food and purrs loudly')
            obj.destroy()
            self._friend = source
            source._companion = self
            Player.clock.register(self.follow, 4)
        else:
            self.location().report(self.name() + ' has no use for that')

    def follow (self,time):
        if not self.is_in_limbo():
            loc = self.location()
            if self._friend and not self._friend.is_in_limbo():
                target = self._friend.location()
                if loc != target:
                    target.report(self.name() + ' follows ' + self._friend.name() + ' to ' + target.name())
                    loc.report(self.name() + ' follows ' + self._friend.name() + ' to ' + target.name())
                    self.move(target)
            else:
                self._friend = None

    def scratch (self):
        if not self.is_in_limbo():
            self.location().report(self.name() + ' tries to protect ' + self._friend.name() + ' and attackes all trolls nearby.')
            for person in self.people_around():
                if person.is_troll():
                    person.suffer(1)

    def suffer (self,hits):
        self.say('me-OW! '+str(hits)+' meow meow meow meow meow meow!')
        self._health -= hits
        if (self.health() <= 0):
            self.die()
        else:
            self.say('meow meow meow meow '+str(self.health()))
            if self._friend:
                self.location().report(self.name()+' runs to '+self._friend.name()+' for comfort.')

    def die (self):
        self.say(':( :( :( :( :(')
        if self._friend:
            self._friend._companion = None
        self.destroy()

    def is_cat (self):
        return True
        
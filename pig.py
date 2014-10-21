import random
from npc import *

class Pig (NPC):

    def __init__ (self,name,loc,desc,restlessness,clumbsiness):
        NPC.__init__(self,name,loc,desc,restlessness,10)
        self._clumbsiness = clumbsiness

        # Register proactive behaviors
        Player.clock.register(self.trip_people, 3)

    def trip_people (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._clumbsiness) == 0:
            people = self.people_around()
            if people:
                victim = random.choice(people)
                self.location().report(self.name() + ' enthusiastically trips ' + victim.name())
                victim.suffer(1)
            else:
                self.location().report(self.name() + ' squeals excitedly')

    def die (self):
        self.say('SQUEEEEeeee...')
        Person.die(self)

    def is_pig (self):
        return True
        
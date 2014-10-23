import random
from npc import *
from food import *

class Pig (NPC):

    def __init__ (self,name,loc,desc,restlessness,clumbsiness):
        Person.__init__(self,name,loc,desc)
        self._restlessness = restlessness
        self._clumbsiness = clumbsiness
        self._sleep_timer = 0

        # Register proactive behaviors
        Player.clock.register(self.move_or_trip, 3)
        Player.clock.register(self.sleep, 4)

    def move_or_trip (self, time):
        if not self.is_in_limbo():
            if self.is_awake():
                if random.randrange(self._restlessness) == 0:
                    self.move_somewhere()
                if random.randrange(self._clumbsiness) == 0:
                    self.trip_people()
            else:
                if self._sleep_timer != 1:
                    self.location().report(self.name() + ' snores softly.')

    def enter_room (self):
        pass

    def trip_people (self):
        people = self.people_around()
        if people:
            victim = random.choice(people)
            self.location().report(self.name() + ' enthusiastically trips ' + victim.name())
            victim.suffer(1)
        else:
            self.location().report(self.name() + ' squeals excitedly')

    def sleep (self, time):
        if not self.is_in_limbo():
            if self._sleep_timer:
                self._sleep_timer -= 1
                if not self._sleep_timer:
                    self.location().report(self.name()+' wakes up from his nap.')

    def is_awake (self):
        return not self._sleep_timer

    def accept (self,obj,source):
        if obj.is_food():
            if self.is_awake():
                self.location().report(self.name() + ' takes the food, squeals happily, and promptly falls asleep.')
                obj.destroy()
                self._sleep_timer = 3
            else:
                self.location().report(self.name()+' snorts sleepily and ignores the food.')
                source.say('Well I guess I\'ll keep it then.')
                obj.move(source)
        else:
            self.location().report(self.name() + ' has no use for that')

    def suffer (self,hits):
        self.say('oink! '+str(hits)+' oink oink oink oink oink oink')
        self._health -= hits
        if (self.health() <= 0):
            self.die()
        else:
            self.say('oink oink oink oink '+str(self.health()))

    def die (self):
        self.say('SQUEEEEeeee...')
        Food('bacon#'+self.name()[-1],self.location(),'Poor ' + self.name() + '...')
        self.destroy()

    def is_pig (self):
        return True
        
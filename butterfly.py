from mobile import *
from player import *
import random

class Butterfly (MobileThing):
    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._flittiness = 2
        self._is_butterfly = False
        self._num_morphs = 0
        self._morph_timer = 3

        # Register proactive behaviors
        Player.clock.register(self.countdown, 1)

    def countdown (self, time):
        self._morph_timer -= 1
        if not self._morph_timer:
            announcement = 'Something odd is happening to '+self.name()+'...'
            if self.location().is_person():
                self.location().location().report(announcement)
            else:
                self.location().report(announcement)
            self.morph()

    def morph (self):
        if not self._num_morphs:
            self._description = 'A cocoon.'
            self._num_morphs += 1
            self._morph_timer = 3
        else:
            self._description = 'A butterfly'
            self._num_morphs += 1
            self._is_butterfly = True
            Player.clock.register(self.fly_around, 2)
            # unregister countdown function

            # Fly out of pocket if someone is holding during transformation
            if self.location().is_person():
                self.location().location().report(self.name()+' flies out of '+self.location().name()+'\'s pocket')
                self.move(self.location().location())


    def fly_around (self, time):
        if random.randrange(self._flittiness) == 0:
            exits = self.location().exits()
            if exits:
                dir = random.choice(exits.keys())
                self.go(dir)

    def go (self,direction):
        loc = self.location()
        exits = loc.exits()
        if direction in exits:
            t = exits[direction]
            loc.report(self.name()+' flies from '+ loc.name()+' to '+t.name())
            self.move(t)
            return True
        else:
            print 'No exit in direction', direction
            return False

    def take (self,actor):
        if not self._is_butterfly:
            actor.say('I take '+self.name()+' from '+self.location().name())
            if self.location().is_person():
                self.location().say('I lose '+self.name())
                self.location().have_fit()
            self.move(actor)
        else:
            actor.say('I try to take ' + self.name() +', but I am too slow')

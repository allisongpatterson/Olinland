from thing import *


class Computer (Thing):
    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)

    def use (self, actor):
        actor.say('I crank up the ol\' computer')
        stuff = actor.check_pocket()
        hws = [x for x in stuff if ('hw-' in x.name() and 'done-' not in x.name())]
        if hws:
            for hw in hws:
                actor.say('I work on ' + hw.name())
                hw.do_hw()
        else:
            actor.say('I do not seem to be carrying anything that needs work')

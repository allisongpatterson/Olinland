from mobile import *


class Wocket (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)

    def use (self,actor):
        actor.say('THERE\'S A WOCKET IN MY POCKET!!!')
        actor.location().report(actor.name() + ' dances a happy little jig')

    def is_wocket (self):
        return True
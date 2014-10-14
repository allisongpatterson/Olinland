from mobile import *
from room import *


class Radar (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)

    def use (self,actor):
        actor.say('I fiddle with the buttons on ' + self.name())
        all_rooms = Room.rooms
        for room in all_rooms:
            room_name = room.name()
            contents = room.contents()
            for thing in contents:
                actor.say('I detect ' + thing.name() + ' in ' + room_name)

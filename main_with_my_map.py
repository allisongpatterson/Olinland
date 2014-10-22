"""Allison Patterson and Jacob Kingery"""

import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from trollhunter import *
from badninja import *
from butterfly import *
from homework import *
from computer import *
from cat import *
from food import *
from pig import *


REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():

    # Outside
    Oval = Room('The Oval','The Center Of Both The Campus And The Swirling Vortex',False)
    GLW = Room('Great Lawn West','Couches Migrate Here In Nice Weather',False)
    GLE = Room('Great Lawn East','Where People Sunbathe In Bikinis Even When There\'s No Actual Sunlight',False)

    # AC
    AC1 = Room('Academic Center First Floor','Here Lurks Room AC128 With Its Cavernous Floors And A Thirst For Sneakers',False)
    AC2 = Room('Academic Center Second Floor','Freshie Central',False)
    AC3 = Room('Academic Center Third Floor','The Awkward Floor Between The Second And The Fourth',False)
    AC4 = Room('Academic Center Fourth Floor','The Elevator\'s Most Frequent Stop',False)

    # MH
    MH1 = Room('Milas Hall First Floor','Part Library, Part Big Awkward Echoey Cavern',False)
    MH2 = Room('Milas Hall Second Floor','Some Offices',False)
    MH3 = Room('Milas Hall Third Floor','Even More Offices!',False)
    MH4 = Room('Milas Hall Fourth Floor','It\'s Entirely Possible That This Floor Doesn\'t Actually Exist',False)

    # DH
    DH = Room('Dining Hall','Food Food Food Food Food',False)
    Mezz = Room('Dining Hall Mezz','That Place Where All The Meetings Happen Because Outlets',False)

    # WH
    WH1 = Room('West Hall First Floor','Foose-Ball, Air Hockey, And Nerf Armory',False)
    WH1W = Room('West Hall First Floor West','That Door Everyone Uses Because It\'s Closer To The DH And We\'re Lazy',False)
    WH1E = Room('West Hall First Floor East','Humble Abode Of The Tatars And Their Tots',False)
    WH1N = Room('West Hall First Floor North','The Semi-Recently Refurbished Kitchen Thanks To Greg And His Infamous Tea Kettle Incident',False)

    WH2 = Room('West Hall Second Floor','Historic Site Of The 2012 Babbie Beating',False)
    WH2W = Room('West Hall Second Floor West','Watch Out For The Drunk Door',False)
    WH2E = Room('West Hall Second Floor East','The Quiet Hallway',False)
    WH2N = Room('West Hall Second Floor North','Home Of The Oddly Named And Beloved Dick-Well',False)

    WH3 = Room('West Hall Third Floor','The Movie Zone',False)
    WH3W = Room('West Hall Third Floor West','Yup',False)
    WH3E = Room('West Hall Third Floor East','Also Yup',False)
    WH3N = Room('West Hall Third Floor North','Also Also Yup',False)

    WH4 = Room('West Hall Fourth Floor','That Place That Had The Chipotle That One Time',False)
    WH4W = Room('West Hall Fourth Floor West','That One Lofted Room That No One Knows Exists',False)
    WH4E = Room('West Hall Fourth Floor East','Party Central',False)
    WH4N = Room('West Hall Fourth Floor North','Coveted Land O\' Lofts',False)

    # EH
    EH1 = Room('East Hall First Floor','The Most-Used Team Rooms Because Nobody Likes Stairs',False)
    EH1W = Room('East Hall First Floor West','Felix\'s Personal Luxury Hotel',False)
    EH1E = Room('East Hall First Floor East','Scotland',False)
    EH1N = Room('East Hall First Floor North','The Infamous Greg Lives Here',False)

    EH2 = Room('East Hall Second Floor','Free Art Stuff For Students With Wellesley Classes And No Monies',False)
    EH2W = Room('East Hall Second Floor West','Forrest',False)
    EH2E = Room('East Hall Second Floor East','Mysterious Voices Float Here',False)
    EH2N = Room('East Hall Second Floor North','Remenants Of The Fallen Society Of Mann Hall',False)

    EH3 = Room('East Hall Third Floor','What Happens Here Is A Mystery',False)
    EH3W = Room('East Hall Third Floor West','More Mystery',False)
    EH3E = Room('East Hall Third Floor East','Even More Mystery!',False)
    EH3N = Room('East Hall Third Floor North','The Poor Souls Who Have To Live Above The Tri-Weekly Tributes To Old Mann Hall',False)

    EH4 = Room('East Hall Fourth Floor','A Roll Of Toilet Paper Dangles From The Ceiling',False)
    EH4W = Room('East Hall Fourth Floor West','Even MORE Mystery!',False)
    EH4E = Room('East Hall Fourth Floor East','EVEN MORE Mystery!',False)
    EH4N = Room('East Hall Fourth Floor North','Home Of Virtually Ever Member Of Olin Robotic Sailing',False)

    # staple it together
    biconnect(Oval,'west',AC1)
    biconnect(Oval,'south',MH1)
    biconnect(Oval,'north',DH)
    biconnect(Oval,'east',GLW)
    biconnect(GLW,'east',GLE)
    biconnect(GLW,'north',WH1)
    biconnect(GLE,'north',EH1)

    biconnect(AC1,'up',AC2)
    biconnect(AC2,'up',AC3)
    biconnect(AC3,'up',AC4)

    biconnect(MH1,'up',MH2)
    biconnect(MH2,'up',MH3)
    biconnect(MH3,'up',MH4)

    biconnect(DH,'up',Mezz)

    biconnect(WH1,'up',WH2)
    biconnect(WH1,'west',WH1W)
    biconnect(WH1,'east',WH1E)
    biconnect(WH1,'north',WH1N)

    biconnect(WH2,'up',WH3)
    biconnect(WH2,'west',WH2W)
    biconnect(WH2,'east',WH2E)
    biconnect(WH2,'north',WH2N)

    biconnect(WH3,'up',WH4)
    biconnect(WH3,'west',WH3W)
    biconnect(WH3,'east',WH3E)
    biconnect(WH3,'north',WH3N)

    biconnect(WH4,'west',WH4W)
    biconnect(WH4,'east',WH4E)
    biconnect(WH4,'north',WH4N)

    biconnect(EH1,'up',EH2)
    biconnect(EH1,'west',EH1W)
    biconnect(EH1,'east',EH1E)
    biconnect(EH1,'north',EH1N)


    # mh353 = Room('Riccardo Office', 'It\'s a bit cramped in here.', False)
    # mh3rd = Room('Milas Hall Third Floor', 'desc', False)
    # mh2nd = Room('Milas Hall Second Floor', 'desc', False)
    # mh1st = Room('Milas Hall First Floor', 'desc', False)
    # oval = Room('Oval', 'The Oval, smack in the center of Olin College.', False)
    # ac1st = Room('Academic Center First Floor', 'desc', False)
    # ac113 = Room('Academic Center 113', 'desc', False)
    # cc1st = Room('Campus Center First Floor', 'desc', False)
    # westh = Room('West Hall', 'The first (and western most) of Olin\'s two dorms.', False)
    # easth = Room('East Hall', 'The second (and eastern most) of Olin\'s two dorms.', False)
    # babson = Room('Babson College', 'Land of the Beavers.', False)
    # dhall = Room('Dining Hall', 'desc', True)

    # biconnect(mh353, 'east',  mh3rd)
    # biconnect(mh3rd, 'down',  mh2nd)
    # biconnect(mh2nd, 'down',  mh1st)
    # biconnect(mh1st, 'north',  oval)
    # biconnect(oval, 'east',  cc1st)
    # biconnect(cc1st, 'east',  westh)
    # biconnect(westh, 'east',  easth)
    # biconnect(oval, 'north',  babson)
    # biconnect(oval, 'west',  ac1st)
    # biconnect(ac1st, 'north',  ac113)

    # biconnect(cc1st, 'east', dhall)

    # The player is the first 'thing' that has to be created

    Player('Blubbering-Fool', Oval, 'player desc')

    # Radar('handy radar', mh353, 'radar desc') 
    # # Radar('handy radar', oval, 'radar desc') 
    # Thing('blackboard', ac113, 'blackboard desc')
    # Thing('lovely-trees', oval, 'trees desc')
    # MobileThing('cs-book', oval, 'cs book desc')
    # MobileThing('math-book', oval, 'math book desc')

    # MobileThing('food', dhall, 'food desc')

    # # Computer('hal-9000', ac113, 'hal-9000 desc')
    # Computer('johnny-5', easth, 'johnny-5 desc')
    # Computer('hal-9000', oval, 'hal-9000 desc')
    # Homework('hw-7', oval, 'work work work')
    # Homework('hw-8', oval, 'work work work')

    # Professor('Riccardo', oval, 'I think he needs some sleep.', random.randint(1,5),2)
    # # Professor('Riccardo', mh353, 'Riccardo desc', random.randint(1,5),2)
    
    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']
    
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms),'Gross.')

    # students = ['Frankie Freshman',
    #             'Joe Junior',
    #             'Sophie Sophomore',
    #             'Cedric Senior']

    # for student in students:
    #     NPC(student,
    #         random.choice(Room.rooms), 
    #         'Look, another Oliner!',
    #         random.randint(1,5),
    #         random.randint(1,5))

    # trolls = ['Polyphemus',
    #           'Gollum']

    # for troll in trolls:
    #   Troll(troll,
    #         random.choice(Room.rooms),
    #         'Big. Ugly. Smelly.',
    #         random.randint(1,3),
    #         random.randint(1,3))

    # Troll('Buttface', oval, 'He\'s a buttface.', 100, 2)

    # Trollhunter('Hunter', oval, 'He\'s a great big manly man.')
    # BadNINJA('Greg', oval, 'I don\'t trust that guy...', 5, 5)
    # Butterfly('Eric', oval, 'He\'s a very hungry caterpillar!')
    # Cat('Felix',oval,'He\'s the best kitty cat EVER!')
    # Food('tuna',oval,'Mmmmm, tuna...')
    # Food('corn', oval, 'Rotary or typewriter? Hmm...')
    # Pig('Pig#1', babson, 'oink', 5, 5)
    # Pig('Pig#2', oval, 'oink oink', 5, 5)
    # Pig('Pig#4', oval, 'oink oink oink oink', 5, 5)

VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down'),
    # for de-bugging purposes.... or for fun
    'kill' : Kill(),
    'hit' : Hit()
}
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'


    # Create the world
    create_world()

    # Register time printer with clock
    Player.clock.register(print_tick_action, 0)
    
    Player.me.look_around()

    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.clock.tick()
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()

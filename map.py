    def make_map():

        # Outside
        Oval = Room('The Oval','The Center Of Both The Campus And The Swirling Vortex')
        GLW = Room('Great Lawn West','Couches Migrate Here In Nice Weather')
        GLE = Room('Great Lawn East','Where People Sunbathe In Bikinis Even When There\'s No Actual Sunlight')

        biconnect(Oval,'west',AC1)
        biconnect(Oval,'south',MH1)
        biconnect(Oval,'north',DH)
        biconnect(Oval,'east',GLW)
        biconnect(GLW,'east',GLE)
        biconnect(GLW,'north',WH1)
        biconnect(GLE,'north',EH1)

        # AC
        AC1 = Room('Academic Center First Floor','Here Lurks Room AC129 With Its Cavernous Floors And A Thirst For Sneakers')
        AC2 = Room('Academic Center Second Floor','Freshie Central')
        AC3 = Room('Academic Center Third Floor','The Awkward Floor Between The Second And The Fourth')
        AC4 = Room('Academic Center Fourth Floor','The Elevator\'s Most Frequent Stop')

        biconnect(AC1,'up',AC2)
        biconnect(AC2,'up',AC3)
        biconnect(AC3,'up',AC4)

        # MH
        MH1 = Room('Milas Hall First Floor','Part Library, Part Big Awkward Echoey Cavern')
        MH2 = Room('Milas Hall Second Floor','Some Offices')
        MH3 = Room('Milas Hall Third Floor','Even More Offices!')
        MH4 = Room('Milas Hall Fourth Floor','I\'m Not Actually Sure If This Floor Exists')

        biconnect(MH1,'up',MH2)
        biconnect(MH2,'up',MH3)
        biconnect(MH3,'up',MH4)

        # DH
        DH = Room('Dining Hall','Food Food Food Food Food')
        Mezz = Room('Dining Hall Mezz','That Place Where All The Meetings Happen Because Outlets')

        biconnect(DH,'up',Mezz)

        # WH
        WH1 = Room('West Hall First Floor','Foose-Ball, Air Hockey, And Nerf Armory')
        WH1W = Room('West Hall First Floor West','That Door Everyone Uses Because It\'s Closer To The DH And We\'re Lazy')
        WH1E = Room('West Hall First Floor East','Humble Abode Of The Tatars And Their Tots')
        WH1N = Room('West Hall First Floor North','The Semi-Recently Refurbished Kitchen Thanks To Greg And His Infamous Tea Kettle Incident')

        WH2 = Room('West Hall Second Floor','A Pretty Poupular Lounge')
        WH2W = Room('West Hall Second Floor West','Formerly The Greatest Hallway Ever')
        WH2E = Room('West Hall Second Floor East','desc')
        WH2N = Room('West Hall Second Floor North','desc')

        WH3 = Room('West Hall Third Floor','desc')
        WH3W = Room('West Hall Third Floor West','desc')
        WH3E = Room('West Hall Third Floor East','desc')
        WH3N = Room('West Hall Third Floor North','desc')

        WH4 = Room('West Hall Fourth Floor','desc')
        WH4W = Room('West Hall Fourth Floor West','That One Lofted Room That No One Knows Exists')
        WH4E = Room('West Hall Fourth Floor East','desc')
        WH4N = Room('West Hall Fourth Floor North','Coveted Land O\' Lofts')

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

        # EH
        EH1 = Room('East Hall First Floor','The Most-Used Team Rooms Because Nobody Likes Stairs')
        EH1W = Room('East Hall First Floor West','Felix\'s Personal Luxury Hotel')
        EH1E = Room('East Hall First Floor East','Scotland')
        EH1N = Room('East Hall First Floor North','desc')

        EH2 = Room('East Hall Second Floor','Free Art Stuff For Students With Wellesley Classes And No Monies')
        EH2W = Room('East Hall Second Floor West','desc')
        EH2E = Room('East Hall Second Floor East','desc')
        EH2N = Room('East Hall Second Floor North','Remenants Of The Fallen Society Of Mann Hall')

        EH3 = Room('East Hall Third Floor','desc')
        EH3W = Room('East Hall Third Floor West','desc')
        EH3E = Room('East Hall Third Floor East','desc')
        EH3N = Room('East Hall Third Floor North')

        EH4 = Room('East Hall Fourth Floor','desc')
        EH4W = Room('East Hall Fourth Floor West','desc')
        EH4E = Room('East Hall Fourth Floor East','desc')
        EH4N = Room('East Hall Fourth Floor North','Home Of Virtually Everyone In Olin Robotic Sailing')

        biconnect(EH1,'up',EH2)
        biconnect(EH1,'west',EH1W)
        biconnect(EH1,'east',EH1E)
        biconnect(EH1,'north',EH1N)

        biconnect(EH2,'up',EH3)
        biconnect(EH2,'west',EH2W)
        biconnect(EH2,'east',EH2E)
        biconnect(EH2,'north',EH2N)

        biconnect(EH3,'up',EH4)
        biconnect(EH3,'west',EH3W)
        biconnect(EH3,'east',EH3E)
        biconnect(EH3,'north',EH3N)

        biconnect(EH4,'west',EH4W)
        biconnect(EH4,'east',EH4E)
        biconnect(EH4,'north',EH4N)
class Board():
    def __init__(self, game):
        """
        This object contains a list of all the coordinates for the SeaFall game board stored in hexgrid_keys.
        """
        self.hexgrid = {}
        
        self.hexgrid_keys = []
        
        self.hexgrid_keys.append("coastal_waters")
        
        self.hexgrid_keys.append("home_harbor_purple")
        
        self.hexgrid_keys.append("home_harbor_red")
        
        self.hexgrid_keys.append("home_harbor_gray")
        
        self.hexgrid_keys.append("home_harbor_blue")
        
        self.hexgrid_keys.append("home_harbor_green")
        
        # row 0
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(0*numpy.ones(9, dtype=numpy.int), numpy.arange(0,9), numpy.arange(0,9))]
        
        # row 1
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(1*numpy.ones(10, dtype=numpy.int), numpy.arange(-1,9), numpy.arange(0,10))]
        
        # row 2
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(2*numpy.ones(9, dtype=numpy.int), numpy.arange(-1,8), numpy.arange(1,10))]
        
        # row 3
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(3*numpy.ones(10, dtype=numpy.int), numpy.arange(-2,8), numpy.arange(1,11))]
        
        # row 4
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(4*numpy.ones(9, dtype=numpy.int), numpy.arange(-2,7), numpy.arange(2,11))]
        
        # row 5
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(5*numpy.ones(10, dtype=numpy.int), numpy.arange(-3,7), numpy.arange(2,12))]
        
        # row 6
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(6*numpy.ones(9, dtype=numpy.int), numpy.arange(-3,6), numpy.arange(3,12))]
        
        # row 7
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(7*numpy.ones(10, dtype=numpy.int), numpy.arange(-4,6), numpy.arange(3,13))]
        
        # row 8
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(8*numpy.ones(9, dtype=numpy.int), numpy.arange(-4,5), numpy.arange(4,13))]
        
        # row 9
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(9*numpy.ones(10, dtype=numpy.int), numpy.arange(-5,5), numpy.arange(4,14))]
        
        # row 10
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(10*numpy.ones(9, dtype=numpy.int), numpy.arange(-5,4), numpy.arange(5,14))]
        
        # row 11
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(11*numpy.ones(10, dtype=numpy.int), numpy.arange(-6,4), numpy.arange(5,15))]
        
        # row 12
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(12*numpy.ones(9, dtype=numpy.int), numpy.arange(-6,3), numpy.arange(6,15))]
        
        # row 13
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(13*numpy.ones(10, dtype=numpy.int), numpy.arange(-7,3), numpy.arange(6,16))]
        
        # row 14
        self.hexgrid_keys = self.hexgrid_keys + \
        [tuple(i) for i in zip(14*numpy.ones(9, dtype=numpy.int), numpy.arange(-7,2), numpy.arange(7,16))]

    def get_valid_moves(self):
        
        return self.valid_moves

    def sail(self, player, ship, destination):

        return True

class Ship():
    def __init__(self, player):
        self.explore = 1
        self.explore_max = 5
        self.hold = 1
        self.hold_max = 5
        self.raid = 1
        self.raid_max = 5
        self.sail = 1
        self.sail_max = 5
        
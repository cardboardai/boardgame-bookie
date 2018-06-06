import networkx as nx
import pandas as pd

PATH_MAP_ADJACENCY_INIT = "map_adjacency_init.xlsx"

class Board():
    def __init__(self, game):
        """
        This object contains a list of all the coordinates for the SeaFall game
        board stored in hexgrid_keys.
        """
        try:
            df = pd.read_excel(PATH_MAP_ADJACENCY_INIT)

        except Exception as e:
            print("Error {}".format(e))
            print("Cannot open *{}*!".format(PATH_MAP_ADJACENCY_INIT))

        self.map = nx.from_pandas.adjacency(df, create_using=nx.DiGraph())


    def get_valid_moves(self):
        
        return self.valid_moves

    def sail(self, player, ship, destination):

        return True


class Ship():
    # Rules, pg 8, "Province Boards" also inlcude information about ships
    def __init__(self):
        self.damage = []
        # hold, a list of objects with max length hold
        self.hold = []
        # upgrades, a list of upgrade objects of max length 2
        self.upgrades = []
        # values (explore, hold, raid, sail)
        self._values = (1, 1, 1, 1)
        # vmax is the maximum number values can reach for (explore, hold, raid,
        # sail)
        self._vmax = (5, 5, 5, 5)

    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self, values):
        if not isinstance(values, tuple):
            err_str = ("Not a valid data type. The data type should be a tuple"
                       " of 4 length.")
            raise ValueError(err_str)
        elif len(values) != 4:
            err_str = ("Not a valid data type. The data type should be a tuple"
                       " of 4 length.")
            raise ValueError(err_str)
        
        for val, vmax in zip(values, self.vmax):
            if val > vmax:
                raise ValueError("A ship value exceeds its max.")

        self._values = values

    @property
    def vmax(self):
        return self._vmax
    
    @vmax.setter
    def vmax(self, vmax_tuple):
        if not isinstance(vmax_tuple, tuple):
            err_str = ("Not a valid data type. The data type should be a tuple"
                       " of 4 length.")
            raise ValueError(err_str)
        elif len(vmax_tuple) != 4:
            err_str = ("Not a valid data type. The data type should be a tuple"
                       " of 4 length.")
            raise ValueError(err_str)

        for val, vmax in zip((5, 5, 5, 5), vmax_tuple):
            if val > vmax:
                raise ValueError("The maximum ship values are never less than (5, 5, 5, 5).")

        self._vmax = vmax


class ProvinceBoard():
    # Rules, pg 8, "Province Boards"
    def __init__(self):
        self.active_advisor = None
        self.at_war_with
        self.building_sites = []
        self.council_room = []
        self.home_enmity
        self.fields = (4, 4)
        ship0 = Ship()
        ship0.values = (2, 3, 2, 2)
        ship1 = Ship()
        ship1.values = (3, 2, 2, 2)
        self.ships = (ship0, ship1)
        self.treasure_room = []
        self.vault = 0
        self.warehouse = []

    def end_of_game():
        return True


class Province():


class Colony():

class Island():

class Upgrade():
    def __init__(self):


class Relic():

class Tablet():

class Goods():

class DicePool():

class Dice():

class Advisor():

class SideBoard():

class Structure():

class Leader():
    # Rules, pg 6, "Leader Cards"
    def __init__(self, appellation=None, fortune=0, improvement=None,
                 name=None, reputation=0, title=None):
        # Rules, pg 6, "Leader Cards"
        # appellation is an ability a leader earns at the start of a campaign
        # or as a game end upgrade.
        self.appellation = appellation
        # Rules, pg 3, "Fortune Tokens"
        # the number of fortune tokens a player has at the begining of a game
        self.fortune = fortune
        # improvement is one of a number of stickers that boosts the effect of
        # a particular guild.
        self.improvement = improvement
        # The name of the leader as given by the player
        self.name = name
        # Rules, pg 3, "Reputation Tokens"
        # the number of reputation tokens a player has at the beginnig of a
        # game.
        self.reputation = reputation
        # Rules, pg 6, "Titles"
        # title, the province rank in the overall campaign based on total
        # glory.
        self.title = title


class Site():
    def __init__(self):

class UpgradeSheet():
    def __init__(self):

class Enmity():
    def __init__(self):
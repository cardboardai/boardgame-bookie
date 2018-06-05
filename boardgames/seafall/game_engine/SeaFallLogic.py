import networkx as nx
import pandas as pd

PATH_MAP_ADJACENCY_INIT = "map_adjacency_init.xlsx"

class Board():
    def __init__(self, game):
        """
        This object contains a list of all the coordinates for the SeaFall game board stored in hexgrid_keys.
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
    def __init__(self, hold=[], upgrades=[], values=(1, 1, 1, 1), vmax=(5, 5, 5, 5)):
        # hold, a list of objects with max length hold
        self.hold = hold
        # upgrades, a list of upgrade objects of max length 2
        self.upgrades = upgrades
        # values (explore, hold, raid, sail)
        self.values = values
        # vmax is the maximum number values can reach for (explore, hold, raid, sail)
        self.vmax = vmax


class Province():
    def __init__(self, player):
        self.field_0 = 4
        self.field_1 = 4

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
    def __init__(self, appellation=None, fortune=0, improvement=None, name=None, reputation=0, title=None):
        # Rules, pg 6, "Leader Cards"
        # appellation is an ability a leader earns at the start of a campaign or as a game end upgrade.
        self.appellation = appellation
        # Rules, pg 3, "Fortune Tokens"
        # the number of fortune tokens a player has at the begining of a game
        self.fortune = fortune
        # improvement is one of a number of stickers that boosts the effect of a particular guild.
        self.improvement = improvement
        # The name of the leader as given by the player
        self.name = name
        # Rules, pg 3, "Reputation Tokens"
        # the number of reputation tokens a player has at the beginnig of a game.
        self.reputation = reputation
        # Rules, pg 6, "Titles"
        # title, the province rank in the overall campaign based on total glory.
        self.title = title


class Site():
    def __init__(self):
        print("hello")

class UpgradeSheet():
    def __init__(self):
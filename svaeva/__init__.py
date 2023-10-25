from svaeva.Paths import Client

from svaeva.Paths.DB.Platforms import Platform
from svaeva.Paths.DB.Groups import Group
from svaeva.Paths.DB.Users import Users
from svaeva.Paths.DB.Actions import Actions
# ----------------------------------------
# MultiAPI
from svaeva.Paths.MultiAPI.Skeletons import Skeleton
from svaeva.Paths.MultiAPI.Configs import Configs
from svaeva.Paths.MultiAPI.VirtualBond import Virtual_Bond
from svaeva.Paths.MultiAPI.Wallet import Wallet
class Panel:

    def __init__(self,token : str = "",end_point : str ="http://localhost:8000"):
        if token != "":
            self.client = Client(token,end_point)
        else:
            self.client = Client()
        self.platform = Platform(self.client)
        self.group    = Group(self.client)
        self.user     = Users(self.client)
        self.actions  = Actions(self.client)
        # MulitAPI
        self.virtual  = Virtual_Bond(self.client)
        self.skeleton = Skeleton(self.client)
        self.config   = Configs(self.client)
        self.wallet   = Wallet(self.client)
from svaeva.Paths import Client

from svaeva.Paths.MultiAPI.Skeletons import Skeleton
from svaeva.Paths.MultiAPI.Configs import Configs
from svaeva.Paths.MultiAPI.VirtualBond import Virtual_Bond
from svaeva.Paths.MultiAPI.Wallet import Wallet

from svaeva.Paths.MultiAPI.Forward import Forward

class MultiAPI:

    def __init__(self,client : Client) -> None:
        self.client = client
        self.virtual  = Virtual_Bond(self.client)
        self.skeleton = Skeleton(self.client)
        self.config   = Configs(self.client)
        self.wallet   = Wallet(self.client)
        self.forward  = Forward(self.client)
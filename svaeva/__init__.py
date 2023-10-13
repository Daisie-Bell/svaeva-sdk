from svaeva.Paths import Client

from svaeva.Paths.DB.Platforms import Platform
from svaeva.Paths.DB.Groups import Group
from svaeva.Paths.MultiAPI.Skeletrons import Skeleton

class Panel:

    def __init__(self,url="",token=""):
        if url != "" and token != "":
            self.client = Client(url=url,key=token)
        else:
            self.client = Client()
        self.platform = Platform(self.client)
        self.group    = Group(self.client)
        self.skeleton = Skeleton(self.client)
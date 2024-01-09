
from svaeva.Paths import Client

from svaeva.Paths.DB.Users     import Users
from svaeva.Paths.DB.Groups    import Group
from svaeva.Paths.DB.Actions   import Actions
from svaeva.Paths.DB.Platforms import Platform 

class DataBase:

    def __init__(self,client : Client) -> None:
        self.client = client
        self.actions = Actions(client)
        self.group = Group(client)
        self.user = Users(client)
        self.platform = Platform(client)
from svaeva.Paths import Client

from svaeva.Paths.DB import DataBase
# ----------------------------------------
# MultiAPI
from svaeva.Paths.MultiAPI import MultiAPI



class Svaeva:

    def __init__(self,token : str = "",end_point : str ="http://localhost:8000"):
        if token != "":
            self.client = Client(token,end_point)
        else:
            self.client = Client()
        # DataBase
        self.database = DataBase(self.client)
        # MulitAPI
        self.multi_api = MultiAPI(self.client)
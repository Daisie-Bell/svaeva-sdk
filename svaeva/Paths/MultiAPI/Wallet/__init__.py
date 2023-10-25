from typing import Any
from svaeva.Paths import Client

class Wallet:

    def __init__(self,client : Client) -> None:
         # Set the client
        self.__dict__["client"] = client
        # Set the session and base_url
        self.__dict__["session"],self.__dict__["base_url"] = self.client.connection
        # Set the path
        self.__dict__["path"] = "/v1/multiapi/wallet"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        temp_params = {}
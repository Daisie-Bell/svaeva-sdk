from typing import Any
from svaeva.Paths import Client

class Wallet:

    def __init__(self,client : Client) -> None:
         # Set the client
        self.__dict__["client"] = client
        # Set the session and base_url
        self.__dict__["session"],self.__dict__["base_url"] = self.client.connection
        # Set the path
        self.__dict__["path"] = "/v1/multiapi/wallets"

    def add_key(self, api_name : str, key : str) -> None:
        for i in range(2):
            try:
                rep = self.session.put(f"{self.base_url}{self.path}",json={api_name:key})
                if rep.status_code == 200:
                    self.__dict__[api_name] = key
                    return rep.json()
                else:
                    raise Exception(rep.json())
            except Exception as e:
                rep = self.session.post(f"{self.base_url}{self.path}",json={"key_wallet":{}})  
                if rep.status_code == 200:
                    print(rep.json())
    
    def remove_key(self, api_name : str) -> None:
        rep = self.session.delete(f"{self.base_url}{self.path}",json={"id":api_name})
        if rep.status_code == 200:
            del self.__dict__[api_name]
            return rep.json()
        else:
            raise Exception(rep.json())

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        temp_params = {}
        if "id" in kwds.keys():
            temp_params.update({"id":kwds["id"]})
        if temp_params == {}:
            response = self.session.get(f"{self.base_url}{self.path}")
        else:
            response = self.session.get(f"{self.base_url}{self.path}",params=temp_params)
        if response.status_code == 200:
            rep = response.json()
            if len(rep) > 1 and isinstance(rep,list):
                for i in rep:
                    i["id"] = i["id"].lower()
                    self.__dict__[i["id"]] = i
            else:
                if isinstance(rep,list):
                    rep = rep[0]
                rep["id"] = rep["id"].lower()
                self.__dict__[rep["id"]] = rep
            return rep
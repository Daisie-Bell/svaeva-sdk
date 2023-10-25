from typing import Any
from svaeva.Paths import Client
from svaeva.Paths.DB.Platforms import Platform

class Users:

    session : Any
    base_url : str

    def __init__(self, client : Client) -> None:
        # Set the client
        self.__dict__["client"] = client
        self.__dict__["platform"] = Platform(client)
        # Set the session and base_url
        self.__dict__["session"],self.__dict__["base_url"] = self.client.connection
        #print(self.session,self.base_url)
        # Set the path
        self.__dict__["path"] = "/v1/db/users"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        temp_params = {}
        for _ in kwds:
            temp_params[_] = kwds[_]
        response = self.session.request("GET",f"{self.base_url}{self.path}",params=temp_params)
        if response.status_code == 200:
            for _ in response.json():
                platform = _["platform"]
                print(platform)
                info = self.platform(id=platform)
                print(info)
                uuid = [_ for _ in info["pf_prams"] if _ in ["username","email","phone_number"]][0]
                if uuid == "username":
                    self.__dict__[str(_["username"])] = _
                elif uuid == "email":
                    name = _["email"].split("@")[0]
                    if "." in name:
                        name = name.replace(".","_")
                    self.__dict__[name] = _
                elif uuid == "phone_number":
                    name = _["phone_number"]
                    if name.startswith("+"):
                        name = name.replace("+","")
                    self.__dict__[name] = _
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        #__value.update({"id":__name})
        response = self.session.request("POST",f"{self.base_url}{self.path}",json=__value)
        if response.status_code == 200:
            info = self.platform(id=__value["platform"])
            print(info)
            uuid = [_ for _ in info["pf_prams"] if _ in ["username","email","phone_number"]][0]
            if uuid == "username":
                name = __value["username"]
            if uuid == "email":
                name = __value["email"].split("@")[0]
                if "." in name:
                    name = name.replace(".","_")
            elif uuid == "phone_number":
                name = __value["phone_number"]
                if name.startswith("+"):
                    name = name.replace("+","")
            self.__dict__[name] = __value
            return self.__dict__[name]
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
        
    def __delattr__(self, __name: str) -> None:
        id_user = self.__dict__[__name]["id"]
        response = self.session.request("DELETE",f"{self.base_url}{self.path}",params={"id":id_user})
        if response.status_code == 200:
            del self.__dict__[__name]
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
        
    @property
    def loaded(self):
        return [_ for _ in self.__dict__.keys() if _ not in ["client","session","base_url","path"]]
    
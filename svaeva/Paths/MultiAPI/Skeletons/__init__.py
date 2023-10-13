from typing import Any
from svaeva.Paths import Client

class Skeleton:

    session : Any
    base_url : str

    def __init__(self, client : Client) -> None:
        # Set the client
        self.__dict__["client"] = client
        # Set the session and base_url
        self.__dict__["session"],self.__dict__["base_url"] = self.client.connection
        #print(self.session,self.base_url)
        # Set the path
        self.__dict__["path"] = "/v1/multiapi/skeletons"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        temp_params = {}
        if "id" in kwds.keys():
            temp_params.update({"id":kwds["id"]})
        if "model_type" in kwds.keys():
            temp_params.update({"model_type":kwds["model_type"]})
        if temp_params != {}:
            response = self.session.get(f"{self.base_url}{self.path}",params=temp_params)
        else:
            response = self.session.get(f"{self.base_url}{self.path}")
        if response.status_code == 200:
            temp = response.json()
            if len(temp) > 1 and isinstance(temp,list):
                for i in temp:
                    i["id"] = i["id"].lower()
                    self.__dict__[i["id"]] = i
            else:
                if isinstance(temp,list):
                    temp = temp[0]
                temp["id"] = temp["id"].lower()
                self.__dict__[temp["id"]] = temp
            return temp
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
        
    def __getattr__(self, name: str) -> Any:
        # Get the attribute
        if self.__dict__.get(name) is None:
            response = self.session.get(f"{self.base_url}{self.path}",params={"id":name})
            self.__dict__[name] = response.json()
        return self.__dict__[name]

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            raise Exception("Cannot overwrite an attribute")
        value.update({"id":name})
        response = self.session.post(f"{self.base_url}{self.path}",json=value)
        if response.status_code == 200:
            self.__dict__[name] = response.json()
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
        
    def __delattr__(self, __name: str) -> None:
        if self.__dict__.get(__name) is None:
            raise Exception("Cannot delete an attribute that does not exist")
        response = self.session.delete(f"{self.base_url}{self.path}",params={"id":__name})
        if response.status_code == 200:
            del self.__dict__[__name]
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
    
    @property
    def loaded(self):
        return [_ for _ in self.__dict__.keys() if _ not in ["client","session","base_url","path"]]
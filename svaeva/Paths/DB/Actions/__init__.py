import json
from typing import Any
from svaeva.Paths import Client

class Actions:

    session : Any
    base_url : str

    def __init__(self, client : Client) -> None:
        # Set the client
        self.__dict__["client"] = client
        # Set the session and base_url
        self.__dict__["session"],self.__dict__["base_url"] = self.client.connection
        #print(self.session,self.base_url)
        # Set the path
        self.__dict__["path"] = "/v1/db/action"
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        temp_params = {}
        if "platform" in kwds.keys():
            temp_params = {"platform":kwds["platform"]}
            if "arg" in kwds.keys():
                temp_params.update({"arg":kwds["arg"]})
            else:
                raise Exception("arg is required")
        elif "group" in kwds.keys():
            temp_params = {"group":kwds["group"]}
        if temp_params != {}:
            response = self.session.get(f"{self.base_url}{self.path}",params=temp_params)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Error: {response.status_code} {response.text}")
        else:
            raise Exception("platform or group is required")
    
    def add(self, __value: Any) -> None:
        response = self.session.post(f"{self.base_url}{self.path}",data=json.dumps(__value))
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")

    def __delattr__(self, __name: str) -> None:
        response = self.client.request("DELETE",f"{self.base_url}{self.path}",params={"id":__name})
        if response.status_code == 200:
            del self.__dict__[__name]
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
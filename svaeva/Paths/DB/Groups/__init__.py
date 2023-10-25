from typing import Any
from svaeva.Paths import Client

class Group:

    session : Any
    base_url : str

    def __init__(self, client : Client) -> None:
        # Set the client
        self.__dict__["client"] = client
        # Set the session and base_url
        self.__dict__["session"],self.__dict__["base_url"] = self.client.connection
        #print(self.session,self.base_url)
        # Set the path
        self.__dict__["path"] = "/v1/db/group"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if "id" in kwds.keys():
            response = self.session.get(f"{self.base_url}{self.path}",params={"id":kwds["id"]})
        else:
            response = self.session.get(f"{self.base_url}{self.path}")
        if response.status_code == 200:
            if isinstance(response.json(),list):
                for i in response.json():
                    self.__dict__[i["id"]] = i
            else:
                self.__dict__[response.json()["id"]] = response.json()
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")

    def __setattr__(self, __name: str, __value: Any) -> None:
        __value.update({"id":__name})
        response = self.session.post(f"{self.base_url}{self.path}",json=__value)
        if response.status_code == 200:
            self.__dict__[__name] = __value
            return self.__dict__[__name]
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
        
    def __delattr__(self, __name: str) -> None:
        response = self.session.delete(f"{self.base_url}{self.path}",params={"id":__name})
        if response.status_code == 200:
            del self.__dict__[__name]
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")

    @property
    def loaded(self):
        return [_ for _ in self.__dict__.keys() if _ not in ["client","session","base_url","path"]]
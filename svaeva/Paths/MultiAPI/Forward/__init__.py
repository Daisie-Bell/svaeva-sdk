from typing import Any
from svaeva.Paths import Client

class Forward:

    session : Any
    base_url : str

    def __init__(self, client : Client) -> None:
        # Set the client
        self.__dict__["client"] = client
        # Set the session and base_url
        self.__dict__["session"],self.__dict__["base_url"] = self.client.connection
        #print(self.session,self.base_url)
        # Set the path
        self.__dict__["path"] = "/v1/multiapi/forward"
    
    def send(self,model_id,input_data):
        response = self.session.post(f"{self.base_url}{self.path}?model={model_id}",json=input_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")
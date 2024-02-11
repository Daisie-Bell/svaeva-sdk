import os
from requests import Session

from dotenv import load_dotenv

load_dotenv()
os.getenv("APIKEY_SVAEVA")

class Client:

    # Requests Base URL
    base_url : str
    # Requests Session Handler
    headers : dict

    def __init__(self,base_url="",key="") -> None:
        self.base_url = base_url
        self.headers = {
            "token":key
        }
        self.env()
    
    def env(self):
        if self.base_url == "":
            self.base_url = "http://{}:{}".format(os.getenv("SVAEVA_IP"),os.getenv("SVAEVA_PORT"))
        if self.headers["token"] == "":
            self.headers["token"] = os.getenv("Svaeva_Key")

    @property
    def connection(self):
        if self.base_url is None:
            raise Exception("Base URL is not set")
        if self.headers["token"] is None:
            raise Exception("Token is not set")
        conn = Session()
        conn.headers.update(self.headers)
        return conn, self.base_url
    
    def set_headers(self,headers):
        self.headers = headers
    
    def set_base_url(self,base_url):
        self.base_url = base_url
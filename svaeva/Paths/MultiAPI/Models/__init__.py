import json
import logging
from typing import Any, Dict

from svaeva import Svaeva
from vrest  import RestAPI

from svaeva.Paths.MultiAPI.Models.Exceptions import InvalidConfig, InvalidKey, InvalidSkeleton

from dotenv import load_dotenv

import os

load_dotenv()

class DataModel:
    
    ai_models : Dict = {}
    configs : Dict = {}
    cash : Dict = {}

    def __init__(self,token):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())
        self.token = token
        self.svaeva = Svaeva("http://{}:8000".format(os.getenv("SVAEVA_IP")),token)
        self.name = self.__class__.__name__

    def add_model(self, name : str) -> None:
        self.ai_models[name] = ""
        self.logger.debug("Model: %s",self.ai_models[name])

    def load_wallet(self):
        self.wallet = self.svaeva.multi_api.wallet()
        self.logger.debug("Wallet: %s",self.wallet)
        for skeletons in self.ai_models:
            try:
                skeleton = self.svaeva.multi_api.skeleton(id=skeletons)
            except Exception as e:
                self.logger.error("Error %s", e)
                self.logger.warning(f"The id ({skeletons}) of the skeleton is not present in Svaeva\n Author: {self.token}")
                raise InvalidSkeleton(skeletons)
            key = [self.wallet["key_wallet"][_] for _ in self.wallet["key_wallet"] if _ == skeletons]
            if len(key) == 0:
                self.logger.warning(f"The key ({skeletons}) of the skeleton is not present in Svaeva\n Author: {self.token}")
                raise InvalidKey(skeletons)
            else:
                self.ai_models[skeletons] = RestAPI(skeleton,key[0])
                self.logger.debug("Model: %s",self.ai_models[skeletons])
    
    def load_config(self,name):
        try:
            self.configs[name] = self.svaeva.multi_api.config(id=name)
            self.logger.debug("Configs: %s",self.configs)
        except Exception as e:
            self.logger.error("Error %s", e)
            self.logger.warning(f"The id ({name}) of the config is not present in Svaeva\n Author: {self.token}")
            raise InvalidConfig(name)

    def load_dataconfig(self,data):
        user_info = self.svaeva.database.user(platform=data["platform"],arg=data["sender"])[0]
        group = self.svaeva.database.group(id=user_info["group_id"])
        self.logger.debug("Group: %s",group)
        self.logger.debug("Data: %s",group["data_config"])
        self.configs = group["data_config"]
        for config in self.configs:
            self.configs[config] = self.svaeva.multi_api.config(id=self.configs[config])
            self.cash.update({config:self.configs[config]})
        self.logger.debug("Configs: %s",self.configs)
        self.logger.debug("Chash: %s",self.cash)
    
    def store(self,data,skeleton,config=None,user=False):
        direction = "model_to_user"
        if user:
            direction = "user_to_model"
        action = {
            "model_id": self.name,
            "skeleton_id": skeleton,
            "config_id": config,
            "user_id": data["sender"],
            "direction": direction,
            "content_data": data[data["type"]],
            "content_text": str(data[data["type"]]),
            "platform": data["platform"]
        }
        self.svaeva.database.actions.add(action)
        self.logger.debug("Action added: %s",action)

    def forward(self,data : Any) -> Any:
        self.logger.debug("Start forwarding")
        self.logger.debug("Data: %s",data)
        self.logger.debug("End forwarding")
        return data
    
    def normalizer(self,data : Any) -> Any:
        if data["type"] == "websocket.receive":
            data = json.loads(data["text"])
        self.logger.debug("Start normalizing")
        self.logger.debug("Data: %s",data)
        self.logger.debug("End normalizing")
        return data
import json
from typing import Any, Dict, List

from svaeva.Paths.MultiAPI.Models import DataModel

from typing import Any


class fuzz_bot(DataModel):
    
    def __init__(self,token) -> None:
        super().__init__()
        self.start(token) # initialize the svaeva client with the user (researcher's) key.
        self.add_model("open_ai") # open_ai skeleton added to svaeva constructed from the JSON blueprint
        self.add_model("deepgram")
        self.load_wallet() # function to load all api keys to call all external APIs, e.g., openAI
        self.load_config("vision") # assigns configuration from svaeva_multi_api.config to the attribute self.configs in DataModel
        self.load_config("auto_deep")
    
    def build_history(self,config,data):
        model = config["config"]["model"]
        targets = {
            "gpt-4-turbo": 128000,
            "gpt-4-vision-preview": 128000,
            "gpt-4": 8192,
            "gpt-4-0613": 8192,
            "gpt-4-32k": 32768,
            "gpt-4-32k-0613": 32768,
            "gpt-3.5-turbo-1106": 16385,
            "gpt-3.5-turbo": 4096,
            "gpt-3.5-turbo-16k": 16384,
            "gpt-3.5-turbo-instruct": 4097,
            "gpt-3.5-turbo-0613": 4096,
            "gpt-3.5-turbo-16k-0613": 16384,
            "text-davinci-003": 4097,
            "text-davinci-002": 4097,
            "code-davinci-002": 8001
        }
        tokens = 0
        target = targets[model]
        list_action = []
        history = self.svaeva.database.actions(user_id=data["sender"],model_id="costume_llm")
        for i in history[::-1]:
            if i["content_type"] == "str":
                tokens += len(i["content_text"])
                if tokens >= target:
                    break
                agent_type = "assistant"
                if i["direction"] == "user_to_model":
                    agent_type = "user"
                list_action.append({
                    "role":agent_type,
                    "content":i["content_text"]
                })
        [config["config"]["messages"].append(_) for _ in list_action[::-1]]
        return config
    
    def normalizer(self,data):
        # strip data from all the json stuff to get text, etc.
        if data["type"] == "websocket.receive":
            data = json.loads(data["text"])
        return data
    def forward(self,data):
        data = self.normalizer(data)

        ########## SPEECH TO TEXT ###########################
        if data["type"] == "voice":
            config_ = self.configs["auto_deep"] # voice model
            audio_text = self.ai_models["deepgram"].pre_recode(params=config_,json={"url":data["voice"]}) # Speech to Text function 
            data["text"] = audio_text.json()["results"]["channels"][0]["alternatives"][0]["transcript"] # get text from deepgram response.
            self.store(data=data,skeleton="deepgram",user=True) # stores the data into the database
            data["type"] = "text"
            data["text"] = 'This is a transcription of a voice message: "{}"'.format(data["text"])
        if data["type"] == "image":
            # Visual Language Model
            self.configs["vision"]["config"]["messages"][0]["content"][1]["image_url"]["url"] = data["image"] # specific to OpenAI API
            # Build the entire history from Actions retrieved from the database.
            llm_history = self.build_history(config=self.configs["vision"], data=data)
            reply = self.ai_models["open_ai"].complete(json=llm_history["config"]) # OpenAI call is 'complete'
            data["text"] = reply.json()["choices"][0]["message"]["content"] # extract text from OpenAI call.
            self.store(data=data, skeleton="open_ai", config="vision") # 
            data["type"] = "text"
            data["image"] = None
            data["text"] = reply.json()["choices"][0]["message"]["content"]
        #
        return self.svaeva.multi_api.forward.send("costume_llm",input_data=data)

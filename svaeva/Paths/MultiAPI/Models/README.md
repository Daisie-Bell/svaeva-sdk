# DataProgramming

## How to use
```python
from dataprogramming import DataModel

class MyModel(DataModel):
    pass
```

## DataModel

### Fuctions

#### `start(token* : str)`
This function is used to start the connection with Svaeva API. It is required to use the API.

##### Backend
```
this function will create:
- self.token (this is the token used to connect to the API)
- self.svaeva (this is the object used to connect to the API)
- self.name = self.__class__.__name__ (this is the name of the model)
```

#### `add_model(model_name* : str)`
This function allows you to add external api models in to your data code.

##### Backend
```
this function adds a key in to a dictionary named ai_models.
- ai_models will contain the VRest objects. (after load_wallet)
```

#### `self.load_wallet() -> None:`
this function will load all your API keys and start the RestAPI Object to interact with the External APIs.

##### Backend
```
this function will call svaeva to get all your API keys for the external APIs;
this function will get all the Skeletons for call external APIs;
this function will update the ai_models dictionary with the VRest objects.
```

#### `get_config(name : str) -> dict:`

this function calls svaeva api to get a configuration to use in your data code.

##### Backend
```
this function will call svaeva to get a config;
this function will update the configs dict with the config.
```

#### `load_dataconfig(data)`
this function will load all your data configurations from the user group.

##### Backend
```
this function will call svaeva to check if is a valid user;
this function will get the group from the user;
this function will get all the data configs from the group;
this function will update the data_configs dict with the data configs.
```

#### `store(self,data,skeleton,config=None,user=False)`
this function will store a action in the database.

##### Backend
```
first will check the direction with user variable; 
this function will build a Dict;
    - {
        "model_id": self.name,
        "skeleton_id": skeleton,
        "config_id": config,
        "user_id": data["sender"],
        "direction": direction,
        "content_data": data[data["type"]],
        "content_text": str(data[data["type"]]),
        "platform": data["platform"]
    }
this function will call svaeva to store the data.
```

#### `normalizer(self,data):`
this function is used to normalize the input data (WebSocket/Post).

##### Backend
```
this function will check if the data is from WebSocket or Post;
this function will normalize the data;
```

#### `forward(self,data):` 
* This Function is used to forward the data to the external APIs.
you need to build your own function to use this function.

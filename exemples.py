from svaeva import Panel

import random
import string


import random
import string


client = Panel()
# Call and __getattr__ (Skeleton)
# Alternative Loading
print(client.skeleton.openai)
# List and load all the available skeletons
print("list and load all the available skeletons")
print(client.skeleton())
# List one skeleton by id
print("List one skeleton by id")
print(client.skeleton(id="openai"))
# List one skeleton by model_type
print("List one skeleton by model_type")
print(client.skeleton(model_type="llm"))
print("list by id and model_type")
print(client.skeleton(id="openai",model_type="llm"))
print("List Loaded skeletons")
print(client.skeleton.loaded)
# Set and __setattr__ (Skeleton)
"""
client.skeleton.elevenlabs = {
    "type_model" : "text2speech",
    "skeleton" : {
        "end_point": "https://api.elevenlabs.io/v1/",
        "header":{
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "*xi-api-key": "{}"
        },
        "skeleton" : {
            "text_to_speech": {
                "suffix": "text-to-speech/{}",
                "method": "POST"
            }
        }
    }
}
"""


def platform():
    """
    This function generates a random uuid and returns it along with a list of random uuid parameters.

    Returns:
    dict: A dictionary containing the generated uuid and a list of random uuid parameters.
    """
    uuids = ["username","email","phone_number"]
    # create a code to generate a random uuid
    rep = {
        "id": ''.join(random.choice(string.ascii_letters) for i in range(10)),
        "pf_prams":[uuids[random.randint(0, len(uuids)-1)]]
    }
    return rep

rep = platform()

client.platform.__setattr__(rep["id"],rep["pf_prams"])
print(client.platform())
while True:
    try:
        for i in client.platform.__dict__:
            if i not in ["client","session","base_url","path"]:
                if len(i) == 10:
                    client.platform.__delattr__(i)
                    print(client.platform())
    except RuntimeError:
        pass
    except Exception as e:
        print(e)
        break
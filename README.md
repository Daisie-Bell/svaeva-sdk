## Svaeva System Delvelopment Kit

### 1. Introduction
This is a system development kit for Svaeva system.
Allow you to intact with SvaevaAPI to build your own Neural Connections across Multi (Agents). 

### 2. Installation

#### 2.1. Install SvaevaAPI
```bash
pip install svaeva
```

#### 2.2. Install SvaevaSDK
```bash
poetry add git+https://github.com/Daisie-lab/SvaevaSDK.git
```

### 3. Usage

#### 3.1. Import SvaevaSDK
```python
from svaeva import Panel
```

> The Panel will contain all Dynamic Objects that you need to build your own Neural Connections.

#### 3.2. Load a Panel
```python
panel = Panel(url="https://api.svaeva.com", token="your_token")
```

#### 3.2.1. Env File
- .env file (in the same directory)
```bash
SVAEVA_URL=https://api.svaeva.com
SVAEVA_TOKEN=<your_token>
```

#### 3.3. Create Skeleton
> To better understand how to create a Skeleton, please refer to [VRest](https://github.com/Vortex5Root/VRest)

#### 3.3.1 To Load Your Skeleton in to the Panel (API)
- Generic Refecence
```python
panel.skeleton.{id} = {
    "type_model": "{define your type model}",
    "skeleton"  : "{vrest skeleton}",
}
```
- Exemple
```python
panel.skeleton.elevenlabs = {
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
# Alternative solution
panel.skeleton.__setattr__("elevenlabs",{
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
})
```
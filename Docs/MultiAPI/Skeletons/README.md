[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Documentation Svaeva SDK (Skeletons)


# Main Documentation

| Topics | SubTopic | SubSubTopic |
| ----- | ----- | ----- |
| [ReadME](../../../README.md) |  |  |
| [Main_Documentation](../../Main.md) |  |  |
|   | DataBase |  |
|   |  └──     | [Platforms](../../DataBase/Platforms/README.md) |
|   |  └──     | [Groups](../../DataBase/Groups/README.md) |
|   |  └──     | [Users](../../DataBase/Users/README.md) |
|   |  └──     | [Actions](../../DataBase/Actions/README.md) |
|   | MultiAPI |  |
|   |  └──     | [Data-Models](../../MultiAPI/DataModels/README.md) |
|   |  └──     | [Virtual_Bounds](../../MultiAPI/Virtual Bounds/README.md) |
|   |  └──     | [Skeletons](../../MultiAPI/Skeletons/README.md) |
|   |  └──     | [Configurations](../../MultiAPI/Configs/README.md) |
|   |  └──     | [Wallets](../../MultiAPI/Wallets/README.md) |

## Documentation Index

| Section | Subsection | Questions |
| ------- | ---------- | ------- |
| [Skeletons](#Skeletons) |  |  |
|    └──  | [Description](#Description) |  |
|    └──  | [Usage](#Usage) |  |
|         | └── | [How to add list of skeletons?](#how-to-add-list-of-skeletons) |
|         | └── | [How to add one skeleton?](#how-to-add-one-skeleton) |
|         | └── | [How to update a skeleton?](#how-to-update-a-skeleton) |
|         | └── | [How to load all skeletons?](#how-to-load-all-skeletons) |
|         | └── | [How to load skeleton by ID?](#how-to-load-skeleton-by-id) |
|         | └── | [How to load all the skeletons to Svaeva?](#how-to-load-all-the-skeletons-to-svaeva) |
|         | └── | [How to delete a skeleton?](#how-to-delete-a-skeleton) |
|    └──  | [License](#License) |  |
|    └──  | [Author](#Author) |  |
|   └──  | [Conclusion](#Conclusion) |  |

### Skeletons

#### Description

Skeleton is a configuration file that contains the API endpoint, headers, and available functions. The svaeva SDK provides a set of methods for managing skeletons:

[Click here to see the documentation of VRest](https://github.com/Daisie-Bell/VRest)

#### Usage

##### How to add list of skeletons?
```python
if client.multi_api.skeleton.loaded == []:
    file_ = open("Blue_paper.json","r")
    skeletons = file_.read()
    skeletons = json.loads(skeletons)
    for i in skeletons:
        row_data = {
            "type_model": skeletons[i]["type_model"],
            "skeleton": skeletons[i]["v_rest"]
        }
        client.multi_api.skeleton.__setattr__(i.lower(),row_data)
```

This code loads a list of skeletons from a JSON file called "Blue_paper.json", converts the JSON data to a Python dictionary, and adds each skeleton to the `Svaeva` object using the `__setattr__` method.

##### How to add one skeleton?

To set skeleton, use the following code:

***All the Skeletons are Stored in a DataBase, so you can use the same skeleton in different projects. Only loading once***

```python
client.multi_api.skeleton.<id> = {
    "type_model": <type_model>,
    "skeleton": <skeleton>
}
```

##### How to update a skeleton?

To update a skeleton, use the following code:

```python
client.multi_api.skeleton.<id> = {
    "type_model": <type_model>,
    "skeleton": <skeleton>
}
```

##### How to load all skeletons?

To list all available skeletons, use the following code:

```python
print(client.multi_api.skeleton())
```

##### How to load skeleton by ID?

To list a specific skeleton by ID or model type, use the following code:

```python
print(client.multi_api.skeleton(id="open_ai"))
print(client.multi_api.skeleton(model_type="llm"))
```

To load a specific skeleton by ID or model type, use the following code:

```python
print(client.multi_api.skeleton.open_ai)
```

##### How to load all the skeletons to Svaeva?

To list all loaded skeletons, use the following code:

```python
print(client.multi_api.skeleton.loaded)
```

##### How to delete a skeleton?

To delete a skeleton, use the following code:

```python
del client.multi_api.skeleton.<id>
```

<a href="#index" class="button">
    <img src="./icons/file-reload-svgrepo-com.svg" alt="Return" width="40" height="40" class="icon">
</a>


## License

This project is licensed under the MIT License - see the [../../LICENSE.md](LICENSE.md) file for details

## Author


[Coder/Manager]

<a href="https://github.com/Vortex5Root">
    <div style="display: flex; justify-content: center; align-items: center; height: 100px; width: 450px;">
        <img src=https://avatars.githubusercontent.com/u/102427260?v=4 width=50 style="border-radius: 50%;"></img>
        <a href="https://github.com/Vortex5Root">Vortex5Root <br><b>        {Full-Stack Software Engineer - Daisie Lab - Svaeva}</b></a>
    </div>
</a>


[Colaborators]

<a href="https://github.com/elacosse">
    <div style="display: flex; justify-content: center; align-items: center; height: 100px; width: 400px;">
        <img src=https://avatars.githubusercontent.com/u/20797023?v=4 width=50 style="border-radius: 50%;">
        <a href="https://github.com/elacosse">elacosse <br><b>{Researcher - Daisie Lab - Svaeva}</b> </a>
    </div>
</a>

### Conclusion

This Documentation is a work in progress. We will continue to update it as we add new features to the svaeva SDK. If you have any questions or suggestions, please feel free to contact us.
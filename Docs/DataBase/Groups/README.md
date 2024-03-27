[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Documentation Svaeva SDK (Groups)


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
|   |  └──     | [Virtual_Bounds](../../MultiAPI/Virtual Bound/README.md) |
|   |  └──     | [Skeletons](../../MultiAPI/Skeletons/README.md) |
|   |  └──     | [Configurations](../../MultiAPI/Configs/README.md) |
|   |  └──     | [Wallets](../../MultiAPI/Wallets/README.md) |

## Documentation Index

| Section | Subsection | Questions |
| ------- | ---------- | ------- |
| [Groups](#Groups) |  |  |
|    └──  | [Description](#Description) |  |
|    └──  | [Usage](#Usage) |  |
|         | └── | [How to add one group?](#How-to-add-one-group) |
|         | └── | [How to update a group?](#How-to-update-a-group) |
|         | └── | [How to load all groups?](#How-to-load-all-groups) |
|         | └── | [How to load group by ID?](#How-to-load-group-by-id) |
|         | └── | [How to load group by model_name?](#How-to-load-group-by-model_name) |
|         | └── | [How to load group by ID?](#How-to-load-group-by-id) |
|         | └── | [How to delete a group?](#How-to-delete-a-group) |
|    └──  | [License](#License) |  |
|    └──  | [Acknowledgments](#Acknowledgments) |  |
|    └──  | [Author](#Author) |  |


### Groups

#### Description

Groups are used to organize the user of your platform. The svaeva SDK provides a set of methods for managing groups:

#### Usage

##### How to add one group?

To set a group, use the following code:

```python
client.database.group.test = {"model_name":"test"}
```

##### How to update a group?

To update a group, use the following code:

```python
client.database.group.test = {"model_name":"test"}
```

##### How to load all groups?

To list all available groups, use the following code:

```python
client.database.group()
```

##### How to load group by ID?

To list a specific group by ID, use the following code:

```python
client.database.group(id="test")
```

##### How to load group by model_name?

To list a specific group by model_name, use the following code:

```python
client.database.group(model_name="test")
```

##### How to load group by ID?

To load a specific group by ID, use the following code:

```python
client.database.group.test
```

##### How to delete a group?

To delete a group, use the following code:

```python
del client.database.group.test
```

<a href="#index" class="button">
    <img src="./icons/file-reload-svgrepo-com.svg" alt="Return" width="40" height="40" class="icon">
</a>

## License

This project is licensed under the MIT License - see the [LICENSE.md](../../LICENSE.md) file for details

## Acknowledgments

-   [Daisie Lab](https://daisie.com/)
-   [Svaeva](https://svaeva.com/)

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
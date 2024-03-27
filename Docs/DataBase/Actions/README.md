[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Documentation Svaeva SDK (Actions)

# Main Documentation

| Topics | SubTopic | SubSubTopic |
| ----- | ----- | ----- |
| [ReadME](../README.md) |  |  |
| [Main_Documentation](../../Main.md) |  |  |
|  └── | [Client](#Client) |  |
|   | └── | [Description](#Description) |
|   | └── | [Usage](#Usage) |
|   | └── | [How to start the client?](#How-to-start-the-client) |
|   | DataBase |  |
|   |  └──     | [Platforms](../DataBase/Platforms/README.md) |
|   |  └──     | [Groups](../DataBase/Groups/README.md) |
|   |  └──     | [Users](../DataBase/Users/README.md) |
|   |  └──     | [Actions](../DataBase/Actions/README.md) |
|   | MultiAPI |  |
|   |  └──     | [Data-Models](../../DataModels/README.md) |
|   |  └──     | [Virtual_Bounds](../../VirtualBounds/README.md) |
|   |  └──     | [Skeletons](../../Skeletons/README.md) |
|   |  └──     | [Configurations](../../Configurations/README.md) |
|   |  └──     | [Wallets](../../MultiAPI/Wallets/README.md) |

## Documentation Index

| Section | Subsection | Questions |
| ------- | ---------- | ------- |
| [Actions](#Actions) |  |  |
|    └──  | [Description](#Description) |  |
|   └──  | [Usage](#Usage) |  |
|         | └── | [How to add one action?](#How-to-add-one-action) |
|         | └── | [How to update a action?](#How-to-update-a-action) |
|         | └── | [How to load all actions?](#How-to-load-all-actions) |
|        | └── | [How to filter actions?](#How-to-filter-actions) |
|       | └── | [How to delete action by ID?](#How-to-delete-action-by-id) |
|   └──  | [License](#License) |  |
|   └──  | [Author](#Author) |  |
|   └──  | [Acknowledgments](#Acknowledgments) |  |


### Actions

#### Description

Actions are used to manage the actions preformed in your platform. The svaeva SDK provides a set of methods for managing actions:

#### Usage

##### How to add one action?

To set an action, use the following code:

```python
client.database.action.add({
    "user_id":"test",
    "group":"test_group",
    "model_id":"costume_llm",
    "skeleton_id":"open_ai",
    "config_id":"jerry",
    "status_message":"test",
    "content_data":"test",
    "content_type":"text",
    "content_text":"test",
})
```

##### How to update a action?

to Update a specific action, use the following code:

```python
client.database.action.update(<json_action>)
```

##### How to load all actions?

To list all available actions, use the following code:

```python
client.database.action()
```

##### How to filter actions?

If you want to filter the actions, use the following code:

Options:
```json
{
    "user_id":<user_id>,
    "group":<group>,
    "model_id":<model_id>,
    "skeleton_id":<skeleton_id>,
    "config_id":<config_id>,
    "status_message":<status_message>,
}
```

you can combine the option as you want.

Example:
```python
client.database.action(user_id="test",group="test_group")
client.database.action(user_id="test",model_id="costume_llm")
client.database.action(user_id="test",skeleton_id="open_ai")
client.database.action(user_id="test",config_id="jerry")
```

##### How to delete action by ID?

To delete a specific action, use the following code:

```python
client.database.action.__delattr__(<id>)
or 
del client.database.action.<id>
```

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
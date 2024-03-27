[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Documentation Svaeva SDK (Platforms)

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
|    └──  | [Platform](#Platform) |  |
|         | └── | [Description](#Description) |
|         | └── | [How to create a platform?](#how-to-create-a-platform) |
|         | └── | [How to update a platform?](#how-to-update-a-platform) |
|         | └── | [How to load all platforms?](#how-to-load-all-platforms) |
|         | └── | [How to load platform by ID?](#how-to-load-platform-by-id) |
|         | └── | [How to delete a platform?](#how-to-delete-a-platform) |
|    └──  | [License](#License) |  |
|    └──  | [Acknowledgments](#Acknowledgments) |  |
|    └──  | [Author](#Author) |  |


### Platform

#### Description

Svaeva SDK includes a `platform` function how allow the user to create and manage his own platforms.

#### How to create a platform?

To set a platform, use the following code:

```python
"""
    Possible arguments:
    {
        "combination": [
            "phone_number",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "description",
            "register_method",
            "country",
            "age",
            "gender",
            "english_proficiency"
        ]
    }
"""
client.database.platform.test = <List[combination]>
```

#### How to update a platform?

To update a platforme make the same as create a platform.

#### How to load all platforms?

To list all available platforms, use the following code:

```python
client.database.platform()
```

#### How to load platform by ID?

To list a specific platform by ID, use the following code:

```python
client.database.platform(id="test")
```

or

To load a specific platform by ID, use the following code:

```python
client.database.platform.test
```

#### How to delete a platform?

To delete a platform, use the following code:

```python
del client.database.platform.test
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
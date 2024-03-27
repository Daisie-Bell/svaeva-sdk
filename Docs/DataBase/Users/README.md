[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Documentation Svaeva SDK (Users)

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
|   |  └──     | [Data-Models](../../DataModels/README.md) |
|   |  └──     | [Virtual_Bounds](../../VirtualBounds/README.md) |
|   |  └──     | [Skeletons](../../Skeletons/README.md) |
|   |  └──     | [Configurations](../../Configs/README.md) |
|   |  └──     | [Wallets](../../MultiAPI/Wallets/README.md) |

## Documentation Index

| Section | Subsection | Questions |
| ------- | ---------- | ------- |
| [Users](#Users) |  |  |
| [Main_Documentation](../../Main.md) |  |  |
|    └──  | [Usage](#Usage) |  |
|         | └── | [How to add one user?](#how-to-add-one-user) |
|         | └── | [How to update a user?](#how-to-update-a-user) |
|         | └── | [How to load all users?](#how-to-load-all-users) |
|         | └── | [How to load user platform and platform uuid?](#how-to-load-user-platform-and-platform-uuid) |
|         | └── | [How to load user by group_id?](#how-to-load-user-by-group_id) |
|         | └── | [How to load user by DB uuid?](#how-to-load-user-by-db-uuid) |
|    └──  | [License](#License) |  |


### Users

#### Description

Users are used to manage the users of your platform. The svaeva SDK provides a set of methods for managing users:

#### Usage

##### How to add one user?

To set a user, use the following code:

```python
client.database.user.test = {
    "platform":"test",
    "username":"test_user",
    "group_id" : "test_group"
}
```

##### How to update a user?

the same as add one user.

##### How to load all users?

To list all available users, use the following code:

```python
client.database.user()
```

##### How to load user platform and platform uuid?

To list a specific user by uuid, use the following code:

```python
client.database.user(platform="test",arg="uuid")
```

##### How to load user by group_id?

To list a specific user by group_id, use the following code:

```python
client.database.user(group="test")
```

##### How to load user by DB uuid?

To load a specific user by uuid, use the following code:

```python
client.database.user.test
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
        <img src=https://avatars.githubusercontent.com/u/102427260?v=4 width=30 style="border-radius: 50%;"></img>
        <a href="https://github.com/Vortex5Root">Vortex5Root <br><b>        {Full-Stack Software Engineer - Daisie Lab - Svaeva}</b></a>
    </div>
</a>


[Colaborators]

<a href="https://github.com/elacosse">
    <div style="display: flex; justify-content: center; align-items: center; height: 100px; width: 400px;">
        <img src="https://avatars.githubusercontent.com/u/20797023?v=4" width="30" style="border-radius: 50%;">
        <a href="https://github.com/elacosse">elacosse <br><b>{Researcher - Daisie Lab - Svaeva}</b> </a>
    </div>
</a>
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Documentation Svaeva SDK (Virtual Bounds)

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
|   |  └──     | [Virtual_Bounds](../../MultiAPI/VirtualBounds/README.md) |
|   |  └──     | [Skeletons](../../MultiAPI/Skeletons/README.md) |
|   |  └──     | [Configurations](../../MultiAPI/Configs/README.md) |
|   |  └──     | [Wallets](../../MultiAPI/Wallets/README.md) |


## Documentation Index

| Section | Subsection | Questions |
| ------- | ---------- | ------- |
| [Virtual Bonds](#Virtual-Bonds) |  |  |
|    └──  | [Description](#Description) |  |
|    └──  | [Usage](#Usage) |  |
|         | └── | [How to add one virtual bond?](#How-to-add-one-virtual-bond) |
|         | └── | [How to update a virtual bond?](#How-to-update-a-virtual-bond) |
|         | └── | [How to load all virtual bonds?](#How-to-load-all-virtual-bonds) |
|         | └── | [How to load virtual bond by ID?](#How-to-load-virtual-bond-by-id) |
|         | └── | [How to delete a virtual bond?](#How-to-delete-a-virtual-bond) |
|    └──  | [License](#License) |  |
|    └──  | [Author](#Author) |  |
|   └──  | [Conclusion](#Conclusion) |  |

### Virtual Bonds

#### Description

Virtual bonds are used to connect multiple APIS allowing the user to create dynamic data flows between different APIS and their components. 

#### Usage

##### How to add one virtual bond?

To set a virtual bond, use the following code:

```python
client.multi_api.virtual.test = {"row_code":"test"}
```

[]

##### How to update a virtual bond?

To update a virtual bond, use the following code:

```python
client.multi_api.virtual.test = {"row_code":"test"}
```

##### How to load all virtual bonds?

To list all available virtual bonds, use the following code:

```python
client.multi_api.virtual()
```

##### How to load virtual bond by ID?

To list a specific virtual bond by ID, use the following code:

```python
client.multi_api.virtual(id="test")
```

or

To load a specific virtual bond by ID, use the following code:

```python
client.multi_api.virtual.test
```

##### How to delete a virtual bond?

To delete a virtual bond, use the following code:

```python
del client.multi_api.virtual.test
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

This documentation is a work in progress and will be updated as the project evolves.
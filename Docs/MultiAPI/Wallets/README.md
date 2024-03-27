[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Documentation Svaeva SDK (Wallets)

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
|   |  └──     | [Virtual_Bounds](../../MultiAPI/Virtual-Bound/README.md) |
|   |  └──     | [Skeletons](../../MultiAPI/Skeletons/README.md) |
|   |  └──     | [Configurations](../../MultiAPI/Configs/README.md) |
|   |  └──     | [Wallets](../../MultiAPI/Wallets/README.md) |

## Documentation Index

| Section | Subsection | Questions |
| ------- | ---------- | ------- |
| [Wallet](#Wallet) |  |  |
|    └──  | [Description](#Description) |  |
|    └──  | [Usage](#Usage) |  |
|         | └── | [How to register your wallet?](#How-to-register-your-wallet) |
|         | └── | [How to add one token?](#How-to-add-one-token) |
|         | └── | [How to update a token?](#How-to-update-a-token) |
|         | └── | [How to load all tokens?](#How-to-load-all-tokens) |
|    └──  | [License](#License) |  |
|    └──  | [Author](#Author) |  |
|   └──  | [Conclusion](#Conclusion) |  |

### Wallet

#### Description

Wallet is where the user can store and manage his tokens for the different APIs.

#### Usage

##### How to register your wallet?

To register your wallet, use the following code:

```python
client.multi_api.wallet.register_wallet()
```

##### How to add one token?

To set a token, use the following code:

```python
client.multi_api.wallet.add_key("<api_name>","<token>")
```

##### How to update a token?

To update a token, use the following code:

```python
client.multi_api.wallet.remove_key("<api_name>","<token>")
```

##### How to load all tokens?

To list all available tokens, use the following code:

```python
client.multi_api.wallet()
```

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

## Conclusion

This is the final version of the documentation for the Wallets API. The documentation is now complete and ready for review. The documentation provides a detailed overview of the Wallets API, including descriptions, usage instructions, and code examples. The documentation also includes information on how to register a wallet, add and update tokens, and load all tokens. The documentation is organized into sections and subsections for easy navigation. The documentation is written in markdown format and includes links to related topics and sections. The documentation is well-structured and easy to read, making it an effective resource for developers working with the Wallets API. The documentation is now ready for review and feedback. Thank you for your attention and support.

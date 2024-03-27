[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/releases)
[![License](https://img.shields.io/github/license/svaeva-sdk/svaeva-sdk)](https://github.com/Daisie-Bell/svaeva-sdk/svaeva-sdk/LICENSE)

# Svaeva System Development Kit (SDK)

## Introduction
| Problem | Solution |
|---------|----------|
| Grounding Language Agents in the real-world  involves  integration across many different data types and calls to external APIs. For instance, integration across audio, visual, and physiological information about a human user. These might occur as real-time data streams. Furthermore, we want to be able to store incoming and generated data in databases that allow easy storage and retrieval, everything from building a simple action history to building a more sophisticated RAG application. How does one easily create a language agent such that we can integrate these multi-modal data streams and data storage/retrieval together with external APIs? | Svaeva tries to solve this problem by allowing developers to construct ways of deploying agents that involves many different kinds of calls to external APIs handling different incoming data types. Essentially, Svaeva is a meta-wrapper around RESTful APIs, connected to a database where incoming requests and outgoing results are stored and managed across different users appropriately. |


## Index

| Section | Subsection | Details |
|---------|------------|---------|
| [Index](#index) |  |  |
| [Dependencies](#dependencies) |  |  |
| [Installation](#installation) |  |  |
| [Glossary of Terminology](#glossary-of-terminology) |  |  |
| [Documentation](#documentation) |  |  |
| [License](#license) |  |  |
| [Acknowledgments](#acknowledgments) |  |  |
| [Authors](#authors) |  |  |
| [Conclusion](#conclusion) |  |  |

## Dependencies

|  python3.11.*  | [python3.11.2](https://www.python.org/downloads/release/python-3112/) |
|-------|-----------|
| <div style="display: flex; justify-content: center; align-items: center; height: 20px; width: 100px;">    <img src=https://python-poetry.org/images/logo-origami.svg width=20 style="border-radius: 50%;"></img><a href="https://python-poetry.org">Poetry</a></div> | 1.5.1 ✅ |
| [requests](https://pypi.org/project/requests/) | ^2.31.0  ✅ | 
| [python-dotenv](https://pypi.org/project/python-dotenv/) | ^1.0.0 ✅ |
| [VRest](https://github.com/Vortex5Root/VRest) | 3.11.*  ✅ | 

## Installation

```bash
poetry add git+https://github.com/Daisie-Bell/svaeva-sdk.git
```

## Glossary of Terminology

Types of Users:
Researchers using Svaeva vs. Clients on Platform

| Terms | Definition | Scope |
|-------|------------|-------------|
| Skeleton | A dictionary with the API endpoint, headers, and available functions. | Researcher |
| Virtual Bond (Data Models) | Python code connecting multiple APIs that define the dynamic data flows between different endpoints and their components. | Researcher |
| Wallet | Store and manage external API keys, i.e., tokens, for the endpoints used. | Researcher |
| Config | The set the parameters for specific skeleton functions, i.e., API endpoints. | Researcher |
| Platform | e.g., WhatsApp, Telegram, allowing clients to interface with Virtual Bonds. | Client |
| Action | JsonModel that store any results from the different APIs and the user interactions. | Client |
| User | Clients that inferface with the platform | Client |
| Group | Group are used to organize the user of your platform. | Client |
| Token-Group | Token-Group is used to handle Svaeva API access group | Root/Researcher |
| Token-User | Token-User is used to give access to Svaeva API to Researchers | Root/Researcher |


## Documentation

Click on the links below to access the documentation for each component of the Svaeva SDK:
[Link](./Docs/Main.md)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

-   [Daisie Lab](https://daisie.com/)
-   [Svaeva](https://svaeva.com/)

## Authors 
[Coder/Manager]

<a href="https://github.com/Vortex5Root">
    <div style="display: flex; justify-content: center; align-items: center; height: 100px; width: 450px;">
        <img src=https://avatars.githubusercontent.com/u/102427260?v=4 width=50 style="border-radius: 50%;">
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

In conclusion, the Svaeva SDK provides a powerful set of functions for managing platforms, groups, users, and actions in your application. With the ability to create, update, load, and delete various entities, you have full control over your platform's data storage and organization. The SDK offers a user-friendly interface and flexible options for filtering and managing actions. 

We would like to express our gratitude to Daisie Lab and Svaeva for their contributions to this project. Their expertise and support have been invaluable in the development of this SDK.

If you have any questions or need further assistance, please refer to the documentation or reach out to our team. We are committed to providing the best possible experience for developers using the Svaeva SDK.

Thank you for choosing Svaeva!

---

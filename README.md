# PDF Editor

Project under development. Last update 19/08/23.

Allows you to edit PDF files for free.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
  - [Commit Message Guidelines](#commit-message-guidelines)
- [Authors](#authors)
- [License](#license)

## About

Briefly describe the project and its main goals.

## Getting Started

Provide information on how to set up and run the project on a local machine.
This will come once I create a User Interface.

For now, getting started guide for myself (for MacOS):
1. Open terminal and `cd` to project folder
2. Activaate virtual environment with `source pdf_editor/bin/activate`
3. Open the project with `charm path/projecct/directory`

### Prerequisites

Built on python 3.10.0.
See [requirements.txt](requirements.txt) for library version information.

TODO: OS information.

### Installation

Step-by-step instructions on how to install and set up the project.
Will come once I built the interface (either for terminal or GUI).

## Usage

Explain how to use the project, including command-line instructions, examples, etc.

## Contributing
Relevant to author. Follow these guidelines to contribute.
### Commit Message Guidelines

To maintain a clean and organized Git history, please use the Conventional Commits style for commit 
messages. [Learn more](https://www.conventionalcommits.org/en/v1.0.0/).

Commit message should be in the form 

`type(scope): summary`
- `type`:

| Type       | Description                                          |
|------------|------------------------------------------------------|
| `feat`     | A new feature.                                      |
| `fix`      | A bug fix.                                          |
| `chore`    | Routine tasks, maintenance, or tooling changes.     |
| `docs`     | Documentation changes.                             |
| `style`    | Code style changes (whitespace, formatting, etc.). |
| `refactor` | Code refactoring (no functional changes).           |
| `test`     | Adding or modifying tests.                         |
| `perf`     | Performance improvements.                         |


- `scope` (Optional): Provides additional context about the part of the codebase affected by the change.
- `summary`: A concise one-line summary in the present tense that describes the change.

Examples:

`feat(user-profile): add profile picture upload feature`

`fix(login): fix incorrect password validation`


## Authors

- Bianca Massacci ([BiancaMass](https://github.com/BiancaMass))

## License

This project is licensed under the [MIT License](LICENSE).
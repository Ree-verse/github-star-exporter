<h1 align="center"><code>github-star-exporter</code> - Export (your) GitHub starred repositories to a JSON file</h1>

A simple CLI to archive your GitHub stars.

## Overview

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Clone the Repository](#1-first-clone-the-repo)
  - [Navigate to the Directory](#2-then-go-to-the-project-folder)
  - [Install the Package](#3-finally-you-can-install-it-locally-with-the-following-command)
- [Usage](#usage)
- [Example](#example)
- [Support](#support)
- [Credits](#credits)
- [Star History](#star-history)
- [License](#license)

## Prerequisites

- Python 3.6 or higher
- `requests`, for making HTTP requests to the GitHub API
- `colorama`, for colored terminal output on all platforms
- A GitHub Personal Access Token (PAT). The PAT must have the `read:user` scope enabled.

## Installation

### 1. First, clone the repo:
- `git clone https://github.com/ree-verse/github-star-exporter.git`

### 2. Then, go to the project folder:
- `cd github-star-exporter`

### 3. Finally, you can install it locally with the following command:
- `pip install .`

> [!NOTE]
> For development, you can also install it in editable mode:
> `pip install -e .`

## Usage

To run with the authenticated user:
```bash
github-star-exporter --token TOKEN
```

To target a specific user:
```bash
github-star-exporter --token TOKEN --user octocat
```

To select a specific output path:
```bash
github-star-exporter --token TOKEN --output /path/to/output.json
```

Here are all available commands:

```console
$ github-star-exporter --help
usage: github-star-exporter [-h] [-t TOKEN] [-u USER] [-o OUTPUT] [-v]

Export (your) GitHub starred repositories to a JSON file.

options:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        GitHub access token (needs read:user permission)
  -u USER, --user USER  Target GitHub username (default: authenticated user)
  -o OUTPUT, --output OUTPUT
                        Output JSON file (default: output.json)
  -v, --version         Version information
```

> [!TIP]
> You can also export all repositories owned by the user instead of starred repos.
> Just change the API endpoint in the code from `/starred` to `/repos`.

## Example

Example output file:

```json
[
    {
        "name": "ReXOR",
        "full_name": "Ree-verse/ReXOR",
        "private": false,
        "html_url": "https://github.com/Ree-verse/ReXOR",
        "description": "Cross-platform Rust library with CLI app implementing XOR encryption/decryption",
        "fork": false,
        "homepage": "https://crates.io/crates/ReXOR",
        "language": "Rust",
        "forks_count": 0,
        "stargazers_count": 1,
        "topics": [
            "cli",
            "decryption",
            "encryption",
            "security",
            "xor"
        ],
        "archived": false,
        "visibility": "public",
        "owner": "Ree-verse",
        "pushed_at": "2025-10-22T11:58:36Z",
        "created_at": "2025-10-22T09:30:23Z",
        "updated_at": "2025-10-22T11:58:39Z",
        "license_name": "MIT License"
    }
]
```

## Support

If you have questions, suggestions, or want to hang out with other developers, join my Discord server: [Ree-verse GitHub Support](https://discord.gg/ZZfqH9Z4uQ).

## Credits

This project was inspired by [JeffCarpenter/export-stars](https://github.com/JeffCarpenter/export-stars).
Many thanks to Jeff Carpenter for the inspiration.

## Star History

<a href="https://star-history.com/#Ree-verse/github-star-exporter&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Ree-verse/github-star-exporter&type=Timeline&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Ree-verse/github-star-exporter&type=Timeline" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Ree-verse/github-star-exporter&type=Timeline" />
  </picture>
</a>

## License

Released under the [MIT License](https://github.com/Ree-verse/github-star-exporter/blob/main/LICENSE) © 2025 [Ree-verse](https://github.com/ree-verse).

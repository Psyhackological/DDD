<div align="center">

  ![Darknet Diaries Downloader](img/DDD_plain.svg)

# Darknet Diaries Downloader

  A CLI-based Python tool for batch downloading episodes of the [Darknet Diaries](https://darknetdiaries.com/) podcast.

  *Because nobody likes being tethered to the Internet while enjoying a good podcast.*

  [![Releases](https://img.shields.io/github/v/release/Psyhackological/DDD?color=000000&style=flat-square)](https://github.com/Psyhackological/DDD/releases)
  [![GPLv3](https://img.shields.io/badge/License-GPL%20v3-FFFFFF.svg)](https://choosealicense.com/licenses/gpl-3.0/)
  [![Python3.7+](https://img.shields.io/badge/python-3.7+-blue.svg?color=FF0000&style=flat-square)](https://www.python.org/downloads/release/python-379/)
  [![CodeQuality](https://img.shields.io/codefactor/grade/github/Psyhackological/DDD/main?color=FFFFFF)](https://www.codefactor.io/repository/github/psyhackological/ddd)
  [![Downloads](https://img.shields.io/github/downloads/psyhackological/ddd/total?color=000000&style=flat-square)](https://github.com/Psyhackological/DDD/releases)

</div>

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [Copyrights](#copyrights)

## Features

- 🎶 **Offline Enjoyment**: Download and listen to episodes without an Internet connection.
- ✅ **Simplicity**: Minimalistic, user-friendly interface.
- 📜 **Extendable**: Export data in JSON format for use in other projects.
- ⌨️ **CLI Support**: Easily download episodes via the command line.

## Installation

### With Git

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Psyhackological/DDD && cd DDD
```

### Without Git

1. Download the ZIP archive from the 'Code' > 'Download ZIP'.
2. Extract the archive and navigate to the project directory.

### Dependencies

Install the required Python modules:

```bash
pip install -r requirements.txt
```

For per-user installation:

```bash
pip install --user -r requirements.txt
```

## Usage

### Basic Help

```bash
python3 DDD.py -h, --help
```

### Download All Episodes

```bash
python3 DDD.py
```

### Download a Range of Episodes

```bash
python3 DDD.py [start] [end]
```

**Example**: Downloading episodes 1 to 10:

```bash
python3 DDD.py 1 10
```

### Download Specific Episodes

```bash
python3 DDD.py -c, --choices [episode_numbers]
```

**Example**: Downloading episodes 3, 5, and 8:

```bash
python3 DDD.py -c 3 5 8
```

## Contributing

No contributions yet, but I'm open to pull requests and suggestions!

## License

![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)

This project is licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).

## Copyrights

This section is a work-in-progress.

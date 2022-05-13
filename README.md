<div align="center">
    <img width="20%" src="img/DDD_plain.svg" alt="DDD_logo">
    <h1>Darknet Diaries Downloader</h1>
    <p>The CLI Python module for bulk downloading the <a href="https://darknetdiaries.com/" target="_blank">Darknet Diaries</a> podcast to a hard memory.</p>
    <p>Hate being online all the time while listening to podcast? This is the way.</p>

[![Releases](https://img.shields.io/github/v/release/Psyhackological/DDD?color=000000&style=flat-square)](https://github.com/Psyhackological/DDD/releases)
[![GPLv3](https://img.shields.io/badge/License-GPL%20v3-FFFFFF.svg)](https://choosealicense.com/licenses/gpl-3.0/)
[![Python3.7+](https://img.shields.io/badge/python-3.7+-blue.svg?color=FF0000&style=flat-square)](https://www.python.org/downloads/release/python-379/)
[![CodeQuality](https://img.shields.io/codefactor/grade/github/Psyhackological/DDD/main?color=FFFFFF)](https://www.codefactor.io/repository/github/psyhackological/ddd)
[![Downloads](https://img.shields.io/github/downloads/psyhackological/ddd/total?color=000000&style=flat-square)](https://github.com/Psyhackological/DDD/releases)

</div>

## Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [Copyrights](#copyrights)

##  Features
- 🎶 Downloading desired files online to enjoy freedom of being offline. 
- ✅ Minimal and easy to use.
- 📜 JSON file can be used your project!
- ⌨️ Intuitive Command Line Interface!

## Installation
### Git way
Open your terminal and paste this line:
```
git clone https://github.com/Psyhackological/DDD && cd DDD
```

### Non-git way
Download zip archive from Code > Download ZIP.

![git_zip](https://imgin.voidnet.tech/uTkmKR8.jpg "git_zip")

There is also source code in [releases](https://github.com/Psyhackological/DDD/releases/) page. (tar.gz and zip archives)

![release_archives](https://imgin.voidnet.tech/8to2Ilh.jpg "release_archives")

###  Dependencies
You need 2 additional modules:
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

They all can be installed at once by pasting this command into the terminal (at the DDD folder):
```
pip install -r requirements.txt
```
Or for current user only:
```
pip install --user -r requirements.txt
```

## Usage
Getting help:
```
python3 DDD.py -h, --help
```

Downloading all episodes:
```
python3 DDD.py
```

Downloading from to episodes:
```
python3 DDD.py start end 
```
__Example:__ Downloading from 1 to 10:
```
python3 DDD.py 1 10 
```

Downloading specific episodes:
```
python3 DDD.py -c, --choices <ints> 
```

__Example:__ Downloading 3 5 8 episodes:
```
python3 DDD.py -c 3 5 8
```

## Contributing
Never have I had one, but I am imperfect human, so I am open for pull requests.

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](https://choosealicense.com/licenses/gpl-3.0/)

Software licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).

## Copyrights
WIP because I do not know how to do this.
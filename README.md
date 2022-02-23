<p align="center">
  <img width="20%" align="center" src="ddd/logo.ico" alt="DDD logo">
</p>
<h1 align="center">D D D </h1>

<p align="center">
    <strong style="font-size: 20px;">D</strong>arknet
    <strong style="font-size: 20px;">D</strong>iaries
    <strong style="font-size: 20px;">D</strong>ownloader
    <br>
    The CLI Python module for bulk downloading the <a href="https://darknetdiaries.com/" target="_blank">Darknet Diaries</a> podcast to a hard memory. <br>
    Hate being online all the time? This is the way.
</p>

<p align="center">
  <a style="text-decoration:none" href="https://github.com/Psyhackological/DDD/releases">
    <img src="https://img.shields.io/github/v/release/Psyhackological/DDD?color=000000&style=flat-square" alt="Releases">
  </a>
  <a style="text-decoration:none" href="https://choosealicense.com/licenses/gpl-3.0/">
      <img src="https://img.shields.io/badge/License-GPL%20v3-FFFFFF.svg" alt="GPLv3">
  </a>
  <a style="text-decoration:none" href="https://www.python.org/downloads/release/python-379/">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg?color=FF0000&style=flat-square" alt="Python Version">
  </a>
  <a style="text-decoration:none" href="https://www.codefactor.io/repository/github/psyhackological/ddd">
    <img src="https://img.shields.io/codefactor/grade/github/Psyhackological/DDD/main?color=FFFFFF" alt="CodeFactor">
  </a>
  <a style="text-decoration:none" href="https://github.com/Psyhackological/DDD/releases">
    <img src="https://img.shields.io/github/downloads/psyhackological/ddd/total?color=000000&style=flat-square" alt="Downloads">
  </a>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#binaries">Binaries</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

##  Features
- Download desired files online and enjoy freedom to be offline.
- Fast and easy to use.
- JSON file can be used in other programming languages.

## Binaries
Pre-built binaries are available from the [releases](https://github.com/Psyhackological/DDD/releases/) page (Windows only).

## Installation
### Git way
Open your terminal and paste this line:
```terminal
git clone https://github.com/Psyhackological/DDD && cd DDD
```

### Non-git way
Download zip archive from Code > Download ZIP.

![git_zip](https://imgin.voidnet.tech/uTkmKR8.jpg "git_zip")

There is also source code in [releases](https://github.com/Psyhackological/DDD/releases/) page. (tar.gz and zip archives)

![release_archives](https://imgin.voidnet.tech/8to2Ilh.jpg "release_archives")

###  Dependencies
Then, you need 2 additional modules:
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

They all can be installed at once by pasting this command into the terminal (at the DDD folder):
```terminal
pip install -r requirements.txt
```
Or for current user only:
```terminal
pip install --user -r requirements.txt
```

## Usage
Getting help:
```terminal
python3 DDD.py -h, --help
```


Downloading all episodes:
```terminal
python3 DDD.py
```


Downloading from to episodes:
```terminal
python3 DDD.py start end 
```
__Example:__ Downloading from 1 to 10:
```terminal
python3 DDD.py 1 10 
```


Downloading specific episodes:
```terminal
python3 DDD.py -c, --choices <ints> 
```

__Example:__ Downloading 3 5 8 episodes:
```terminal
python3 DDD.py -c 3 5 8
```

## Contributing
Never have I had one, but I am imperfect human, so I am open for pull requests.

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](https://choosealicense.com/licenses/gpl-3.0/)

Software licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).
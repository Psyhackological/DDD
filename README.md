<p align="center">
  <img width="20%" align="center" src="ddd/logo.ico" alt="DDD logo">
</p>
<h1 align="center">D D D </h1>

<p align="center">
    <strong style="font-size: 20px;">D</strong>arknet
    <strong style="font-size: 20px;">D</strong>iaries
    <strong style="font-size: 20px;">D</strong>ownloader
    <br>
    The CLI Python module for bulk downloading the <a href="https://darknetdiaries.com/" target="_blank">Darknet Diaries</a> podcast to a hard disc.
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
    <li><a href="#installation">Installation</a></li>
    <li><a href="#dependencies">Dependencies</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

##  Features
- Download desired files online and enjoy freedom to be offline.
- Fast and easy to use.
- JSON file can be used in other programming languages.

## Installation
Pre-built binaries are available from the [releases](https://github.com/Psyhackological/DDD/releases/) page.

##  Dependencies
You need 2 additional modules:
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

They all can be installed at once by pasting this command into the terminal (at the DDD folder):
```terminal
pip install -r requirements.txt
```
If the installation fails due to lack of access rights, try this:
```terminal
pip install --user -r requirements.txt
```

## Usage
Paste this command into the terminal (at the DDD folder):
```terminal
python DDD.py
```

## Contributing
Never have I had one, but I am imperfect human, so I am open for pull requests.

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](https://choosealicense.com/licenses/gpl-3.0/)

Software licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).
# Extract Informations From Mails - (Python)

## Description

This project is a simple application that extracts information from emails and stores them in a excel file.

## Table of Contents

- [Installation](#installation)
  - [Python](#python)
    - [Create a virtual environment](#create-a-virtual-environment)
    - [Activate virtual environment](#activate-virtual-environment)
  - [Poetry](#poetry)
    - [Add a package](#add-a-package)
    - [Remove a package](#remove-a-package)
    - [Update a package](#update-a-package)
    - [Install all packages](#install-all-packages)
    - [Update the requirements.txt file after adding or removing a package](#update-the-requirementstxt-file-after-adding-or-removing-a-package)
  - [Generate executable](#generate-executable)

---

# Installation

## Python

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

```bash
.\.venv\Scripts\activate.ps1
```

## Poetry

### Add a package

```bash
poetry add <package_name>
```

### Remove a package

```bash
poetry remove <package_name>
```

### Update a package

```bash
poetry update <package_name>
```

### Install all packages

```bash
poetry install
```

### Update the requirements.txt file after adding or removing a package

```bash
poetry run pip freeze > requirements.txt
```

## Generate executable

```bash
pyinstaller --onefile <"path to main.py">
```

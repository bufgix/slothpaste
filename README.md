# Sloth
A simple file content sharing app.

## Installation
```bash
$ pip install sloth-paste
```

## Usage
```bash
$ sloth -h
usage: sloth [-h] [-p POSTER] [--syntax SYNTAX] [--exp {day,week,year}] [-u]
             file [file ...]

Code sharing app for lazy people.

positional arguments:
  file                  File to share content

optional arguments:
  -h, --help            show this help message and exit
  -p POSTER, --poster POSTER
                        Author name
  --syntax SYNTAX       Desired syntax (py, js, cpp...)
  --exp {day,week,year}
                        Expiration time
  -u, --update-db       Update suported langs from paste.ubuntu.com
```

```bash
sloth setup.py test.py -p bufgix
[i] 2 files entered...
[i] Poster: bufgix...
==============================
[i] File: setup.py
[i] Detected language python3
[+] Paste link: https://paste.ubuntu.com/p/4Jm6gVNbQ4/

==============================

[i] File: test.py
[i] Detected language python3
[+] Paste link: https://paste.ubuntu.com/p/JV4yPXMDc6/

==============================

Copied last link: https://paste.ubuntu.com/p/JV4yPXMDc6/
```

## LICENSE
[MIT](https://github.com/bufgix/slothpaste/blob/master/LICENSE)


# basic-pass-import
Very basic importer for [pass](https://www.passwordstore.org/), the standard unix password manager

One of my first python projects in a very long time. 

This its a basic script that takes a text file with passwords in the form of `name|password` and inserts them into pass. Note you must have already setup pass with `pass init`. The need for me came from moving away from a graphical password manager I was using, Padlock, to a command line only solution. I spend way less time fiddling around opening a program and logging in now that I use pass, its great! 

## Usage: 
`passimport example.csv`

## Build / Install:
1. `pipenv install`
1. `pipenv shell`
1. `pyinstaller --onefile -c passimport.py`
1. `cp dist/passimport /usr/local/bin`

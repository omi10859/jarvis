
<img width="350" alt="portfolio_view" src="https://user-images.githubusercontent.com/26123416/41307339-8701e1e2-6e96-11e8-8bbd-d938c45caf26.png">

[![Built with ❤](https://forthebadge.com/images/badges/built-with-love.svg)](https://omkar.site/)
[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)]()
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
<br>
Welcome to my source code 🙈<br>
I'm written in python.<br>


## What is GROOT?
GROOT is a virtual assistant which functioning with voice recognition.

## What GROOT can do?
A virtual assistant basically tries to recognize voice of a person and 
then implement the task said by the invoker.

Functions of GROOT are-
* Play videos on youtube on your voice command.
   > Play video name on youtube

* Open any URL.
   >Hey GROOT Can you please open random.in
     (You dont need to include www)


## How to Contribute to GROOT?
To contribute to GROOT,<br>
Go to the following repository<br>
https://github.com/omi10859/GROOT

Feel free to open an issue or recommend any changes which you want to see in the website.
Adhere to the guidelines mentioned below if you want to contribute.

## Guidelines

* Make sure your PR contains one logical change only!
* In case there are multiple commits in your PR squash them into one. Ref :
* https://makandracards.com/makandra/527-squash-several-git-commits-into-a-single-commit
* Make sure you update your REMOTE ORIGIN in case you have forked this repo :
* https://help.github.com/articles/syncing-a-fork/
* Once you update the forked repo make sure you rebase the changes and then open the PR.
* Ref: http://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository
* Upload Screenshot(s) or provide a link to working demo of the website while making a PR.

## Installation
Clone the repository. Then, follow the installation steps to talk GROOT.

## How to run GROOT?
The source code of GROOT is written in python.

### Create a Virtual Environment(python --version 3.6 required)
```
virtualenv -p python3.6 VENV_NAME
```
### Activate the venv
Windows: `VENV_NAME/Scripts/activate`

Linux: `source VENV_NAME/bin/activate`

Mac: `source VENV_NAME/bin/activate`

### For linux users

sudo apt-get install python3.6-dev
sudo apt-get install python3.6-tk

### Install dependencies

```pip install -r requirements/requirements[mac/linux/win] ```

### TODO list-

* [x] Basic GUI
* [x] Text-to-speech
* [x] speech-to-text
* [x] Voice commands
* [x] Text commands
* [ ] [Rethinking GUI](https://github.com/omi10859/GROOT/issues/8)
* Modules:
    * [x] Playing Songs on YouTube with voice commands
    * [x] Opening URLs in Browser
    * [ ] Presenting answers to questions
    * [ ] LIVE weather
    * [ ] Translations
    * [ ] [Add more](https://github.com/omi10859/GROOT/issues/new)
* [ ] Adding "Always listening feature"
* [ ] Changing Brightness and Redness on command

## Enjoy talking GROOT 
```python Gui.py```


## To use microphone in linux unmute all channels by opening Alsamixer

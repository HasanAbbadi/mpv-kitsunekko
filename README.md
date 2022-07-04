# Kitsu
A python file and an [mpv](https://mpv.io) script to download subtitles

from [KitsuNekko](https://kitsunekko.net/) for current playing episode.


By default it downloads Japanese subtitles, if you want to change that

edit `kitsu.py` and change `language = 'japanese'` to your preferred language.

## Usage
-----
Press `Ctrl-k` while playing an episode to start the script.
(you can change the keybinding from `main.lua` file)

Or you can use the python file independently, as follows:
```bash
python3 kitsu.py [path/to/video/file]
```

## Installation
-----
Make sure you have the dependencies installed:
  * mpv >= 27.0
  * python 3.x
  * python-requests
  * python-beautifulsoup4

Then curl this repository into your `scripts` folder:
```bash
curl https://github.com/HasanAbbadi/mpv-kitsunekko ~/.config/mpv/scripts/kitsu
```

import sys, os, re
import requests
from bs4 import BeautifulSoup
import difflib
import urllib
from urllib.parse import quote

# *lowercase*, available: english, japanese, chinese, korean
language = 'japanese'

if sys.argv[1] == "" or None:
  print("No file playing")
  sys.exit()

def get_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    strong_list = soup.find_all('strong')
    anime_list = []
    for anime in strong_list:
        anime_list.append(anime.text.strip())
    return anime_list

if language is 'english':
    url  = 'https://kitsunekko.net/dirlist.php?dir=subtitles%2F'
    url2 = 'https://kitsunekko.net/subtitles/'
else:
    url =  'https://kitsunekko.net/dirlist.php?dir=subtitles%2F%s%2F' % (language)
    url2 = 'https://kitsunekko.net/subtitles/%s' % (language)

anime_list = get_list(url)

anime = sys.argv[1]
matches = difflib.get_close_matches(anime, anime_list)

if not matches:
    print('No such anime, try cleaning the video name')
    sys.exit()

best_match = quote(matches[0].encode("utf-8"))

url += best_match
ep_list = get_list(url)

anime_ep = re.findall(r'\d+', anime)
compressed = ('zip', '7z', 'rar')

if len(anime_ep):
    # if current anime episode num == episode of subtitle > put in array.
    files = [ (s) for s in ep_list if anime_ep[-1] == re.findall(r'\d+', s)[-1] ]
else:
    # if subtitle file ends with a compression extension  > put in array.
    files = [ (s) for s in ep_list if s.endswith(compressed) ]

if not len(files):
    print('Unfortunately, nothing was found.')
    sys.exit()

best_file = quote(files[0].encode("utf-8"))
ext = files[0].split('.')[-1]

file_name = '.'.join(sys.argv[1].split('.')[:-1])
full_path = '%s.%s' % (file_name, ext)
print("Downloaded file: " + full_path)

url = '%s/%s/%s' % (url2, best_match, best_file)
urllib.request.urlretrieve(url, full_path)

if full_path.endswith(compressed):
    print("Downloaded file is a compressed file;")
    print("Not yet implemented.")
    sys.exit()

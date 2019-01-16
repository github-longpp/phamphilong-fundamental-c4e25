import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL 
url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")

ul_songs = soup.find_all("ul")
ul_songs = ul_songs[3]


li_list = ul_songs.find_all("li")
songs_list = []
for li in li_list:
    song_name = li.h3.a.string
    artist = li.h4.a.string
    songs = {
        "Song name" : song_name,
        "Artist" : artist
    }
    songs_list.append(songs)

    search = str(song_name) + " " + str(artist)

    print(search)
    options = {
            'default_search': 'ytsearch', 
            'max_downloads': 1 
        }
    dl = YoutubeDL(options)
    dl.download(search)

 
pyexcel.save_as(records = songs_list, dest_file_name = "Top100song.xlsx")

    
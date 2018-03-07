import media
import fresh_tomatoes
import urllib2
import json

key_api = 'fe09bc7261fdf7e9378f67ccbeeb84e1'

# Fetching Gladiator data from API service
try:
    glad_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/98?api_key="+key_api)
    gladvid_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/98/videos?api_key="+key_api)
except urllib2.HTTPError, e:
    checksLogger.error('HTTPError = ' + str(e.code))

glad_data = json.load(glad_obj)
gladvid_data = json.load(gladvid_obj)

for item in gladvid_data["results"]:
    glad_yt_key = item["key"]

# Creating Gladiator object
gladiator = media.Movie(glad_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+glad_data["poster_path"],
	"https://www.youtube.com/watch?v="+glad_yt_key)

# Fetching Godfather data from API service
try:
    god_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/238?api_key="+key_api)
    godvid_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/238/videos?api_key="+key_api)
    except urllib2.HTTPError, e:
    checksLogger.error('HTTPError = ' + str(e.code))

god_data = json.load(god_obj)
godvid_data = json.load(godvid_obj)

for item in godvid_data["results"]:
    god_yt_key = item["key"]

# Creating Godfather object
the_godfather = media.Movie(god_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+god_data["poster_path"],
	"https://www.youtube.com/watch?v="+god_yt_key)

# Fetching fightclub data from API service
try:
    fc_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/550?api_key="+key_api)
    fcvid_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/550/videos?api_key="+key_api)
except urllib2.HTTPError, e:
    checksLogger.error('HTTPError = ' + str(e.code))

fc_data = json.load(fc_obj)
fcvid_data = json.load(fcvid_obj)

for item in fcvid_data["results"]:
    fc_yt_key = item["key"]

# Creating fightclub object
twelve_monkeys = media.Movie(fc_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+fc_data["poster_path"],
	"https://www.youtube.com/watch?v="+fc_yt_key)

# Fetching Cuckoo data from API service
try:
    cuck_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/510?api_key="+key_api)
    cuckvid_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/510/videos?api_key="+key_api)
except urllib2.HTTPError, e:
    checksLogger.error('HTTPError = ' + str(e.code))

cuck_data = json.load(cuck_obj)
cuckvid_data = json.load(cuckvid_obj)

for item in cuckvid_data["results"]:
    cuck_yt_key = item["key"]

# Creating Cuckoo object
cuckoo_nest = media.Movie(cuck_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+cuck_data["poster_path"],
	"https://www.youtube.com/watch?v="+cuck_yt_key)

# Fetching Matrix data from API service
try:
    mat_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/603?api_key="+key_api)
    matvid_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/603/videos?api_key="+key_api)
except urllib2.HTTPError, e:
    checksLogger.error('HTTPError = ' + str(e.code))

mat_data = json.load(mat_obj)
matvid_data = json.load(matvid_obj)

for item in matvid_data["results"]:
    mat_yt_key = item["key"]

# Creating Matrix object
the_matrix = media.Movie(mat_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+mat_data["poster_path"],
	"https://www.youtube.com/watch?v="+mat_yt_key)

# Fetching American Beauty data from API service
try:
    ame_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/14?api_key="+key_api)
    amevid_obj = urllib2.urlopen(
    "https://api.themoviedb.org/3/movie/14/videos?api_key="+key_api)
except urllib2.HTTPError, e:
    checksLogger.error('HTTPError = ' + str(e.code))

ame_data = json.load(ame_obj)
amevid_data = json.load(amevid_obj)

for item in amevid_data["results"]:
    ame_yt_key = item["key"]

# Creating American Beauty object
american_beauty = media.Movie(ame_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+ame_data["poster_path"],
	"https://www.youtube.com/watch?v="+ame_yt_key)

movies = [the_godfather,
twelve_monkeys,
the_matrix,
american_beauty,
gladiator,
cuckoo_nest]

fresh_tomatoes.open_movies_page(movies)
